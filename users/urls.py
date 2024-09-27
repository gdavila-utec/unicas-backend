from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, get_user_info, get_users_from_junta

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/info', get_user_info ),
    path('api/junta-users/<int:junta_id>/', get_users_from_junta),
]
