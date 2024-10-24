import datetime
import logging
from dotenv import load_dotenv
import jwt
import pytz
import requests
from django.contrib.auth import get_user_model
from users.models import CustomUser as User
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import os
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from jwt import algorithms
from jwt import PyJWKClient

load_dotenv()
User = get_user_model()

CLERK_API_URL = "https://api.clerk.com/v1"
CLERK_FRONTEND_API_URL = os.getenv("CLERK_FRONTEND_API_URL")
CLERK_SECRET_KEY = os.getenv("CLERK_SECRET_KEY")
CLERK_JWKS_URL = os.getenv("CLERK_JWKS_URL")
CACHE_KEY = "jwks_data"
CLERK_ISSUER = os.getenv("CLERK_ISSUER")

logger = logging.getLogger(__name__)

class JWTAuthenticationMiddleware(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None
        try:
            token = auth_header.split(" ")[1]
            logger.info(f"Received token: {token}")
        except IndexError:
            raise AuthenticationFailed("Bearer token not provided.")
        user = self.decode_jwt(token)
        if not user:
            return None

        clerk = ClerkSDK()
        info, found = clerk.fetch_user_info(user.username)
        if found:
            user.email = info["email_address"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.last_login = info["last_login"]
            user.save()

        return user, None

    def decode_jwt(self, token):
        try:
            # First decode without verification to log the claims
            unverified_payload = jwt.decode(
                token,
                options={"verify_signature": False},
                algorithms=["RS256"]
            )
            logger.info(f"Token issuer: {unverified_payload.get('iss')}")
            logger.info(f"Token audience: {unverified_payload.get('aud')}")

            jwks_client = PyJWKClient(CLERK_JWKS_URL)
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                options={
                    "verify_signature": True,
                    "verify_aud": False,
                    "verify_iss": True,
                },
                issuer="https://sincere-dogfish-4.clerk.accounts.dev" 
            )
            logger.info(f"Decoded payload: {payload}")
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired.")
        except jwt.DecodeError as e:
            logger.error(f"Token decode error: {str(e)} - Token: {token}")
            raise AuthenticationFailed("Token decode error.")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token.")
        except Exception as e:
            logger.error(f"Unexpected error during JWT decoding: {str(e)}")
            raise AuthenticationFailed("Authentication failed.")

        user_id = payload.get("sub")
        if user_id:
            user, created = User.objects.get_or_create(username=user_id)
            return user
        return None

class ClerkSDK:
    def fetch_user_info(self, user_id: str):
        try:
            response = requests.get(
                f"{CLERK_API_URL}/users/{user_id}",
                headers={"Authorization": f"Bearer {CLERK_SECRET_KEY}"},
            )
            response.raise_for_status()
            data = response.json()
            return {
                "email_address": data["email_addresses"][0]["email_address"],
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "last_login": datetime.datetime.fromtimestamp(
                    data["last_sign_in_at"] / 1000, tz=pytz.UTC
                ),
            }, True
        except requests.RequestException as e:
            logger.error(f"Error fetching user info from Clerk: {str(e)}")
            return {
                "email_address": "",
                "first_name": "",
                "last_name": "",
                "last_login": None,
            }, False

    def get_jwks(self):
        jwks_data = cache.get(CACHE_KEY)
        if not jwks_data:
            try:
                logger.info(f"Fetching JWKS from URL: {CLERK_JWKS_URL}")
                response = requests.get(CLERK_JWKS_URL)
                response.raise_for_status()
                jwks_data = response.json()
                logger.info(f"JWKS response: {response.text}")
                cache.set(CACHE_KEY, jwks_data, timeout=3600)  # cache for 1 hour
            except requests.RequestException as e:
                logger.error(f"Failed to fetch JWKS: {str(e)}")
                raise AuthenticationFailed("Failed to fetch JWKS.")
            except ValueError as e:
                logger.error(f"Invalid JSON in JWKS response: {str(e)}")
                raise AuthenticationFailed("Invalid JWKS data.")
        return jwks_data
