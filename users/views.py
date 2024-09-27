from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAdminUser
from .serializer import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from juntas.models import Junta
User = get_user_model()
from .permissions import IsAdminOrReadOnly, IsFacilitatorOrReadOnly, IsDirectorOrReadOnly, IsPartnerOrReadOnly

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


