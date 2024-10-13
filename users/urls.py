from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, get_user_info, get_users_from_junta, get_member_by_dni, get_member_prestamos, get_member_pagos, get_member_multas, get_member_acciones

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/info', get_user_info ),
    path('api/junta-users/<int:junta_id>/', get_users_from_junta),
    path('api/members/dni/<str:dni>/', get_member_by_dni),
    path('api/members/dni/<str:dni>/prestamos/', get_member_prestamos),
    path('api/members/dni/<str:dni>/pagos/', get_member_pagos),
    path('api/members/dni/<str:dni>/multas/', get_member_multas),
    path('api/members/dni/<str:dni>/acciones/', get_member_acciones),
]
