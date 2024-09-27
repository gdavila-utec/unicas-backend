from rest_framework import serializers
from .models import CustomUser

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "email", "first_name", "last_name",  "id",
            "is_superuser",
            "document_type", "full_name", "document_number", "birth_date",
            "province", "district", "address", "shares", "username"
        ]
