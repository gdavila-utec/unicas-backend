from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'full_name', 'birth_date')}),
        ('Document info', {'fields': ('document_type', 'document_number')}),
        ('Location', {'fields': ('province', 'district', 'address')}),
        ('Shares', {'fields': ('shares',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'document_type', 'document_number', 'birth_date', 'province', 'district', 'address', 'shares'),
        }),
    )
    list_display = ('username','email', 'first_name', 'last_name', 'is_staff','is_superuser', 'id')


admin.site.register(CustomUser, CustomUserAdmin)