from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAdminUser
from .serializer import UserSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from juntas.models import Junta
User = get_user_model()
from .permissions import IsAdminOrReadOnly, IsFacilitatorOrReadOnly, IsDirectorOrReadOnly, IsPartnerOrReadOnly
from prestamos.serializers import PrestamoSerializer, PagosPrestamosSerializer
from multas.serializers import MultaSerializer
from prestamos.models import Prestamo, PagosPrestamos
from acciones.serializers import AccionPurchaseSerializer, AccionPurchase
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    #     IsAdminOrReadOnly | IsFacilitatorOrReadOnly | IsDirectorOrReadOnly | IsPartnerOrReadOnly
    # ]
    permission_classes = [
        IsAdminUser
    ]
    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [IsAdminOrReadOnly | IsFacilitatorOrReadOnly]
    #     elif self.action == 'retrieve':
    #         permission_classes = [IsAdminOrReadOnly | IsFacilitatorOrReadOnly | IsDirectorOrReadOnly | IsPartnerOrReadOnly]
    #     else:
    #         permission_classes = [IsAdminOrReadOnly]
    #     return [permission() for permission in permission_classes]

@api_view(['GET'])
def get_users_from_junta(request, junta_id):
    junta = Junta.objects.filter(id=junta_id).first()
    if junta:
        users = junta.members.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response({"error": "Junta not found"}, status=404)

@api_view(['GET'])
def get_user_info(request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def get_member_by_dni(request, dni):
    try:
        member = User.objects.filter(document_number=dni).first()
        serializer = UserSerializer(member)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def get_member_prestamos(request, dni):
    try:
        user = User.objects.filter(document_number=dni).first()
        prestamos = Prestamo.objects.filter(member=user)
        serializer = PrestamoSerializer(prestamos, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def get_member_pagos(request, dni):
    try:
        user = User.objects.filter(document_number=dni).first()
        prestamos = Prestamo.objects.filter(member=user)
        pagos = PagosPrestamos.objects.filter(prestamo__in=prestamos)
        serializer = PagosPrestamosSerializer(pagos, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def get_member_multas(request, dni):
    member = User.objects.filter(document_number=dni).first()
    multas = member.multas.all()
    serializer = MultaSerializer(multas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def get_member_acciones(request, dni):
    try:
        user = User.objects.filter(document_number=dni).first()
        acciones = AccionPurchase.objects.filter(member=user)
        serializer = AccionPurchaseSerializer(acciones, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
