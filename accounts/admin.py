from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "username",
        "email",
        "phone",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    fieldsets = UserAdmin.fieldsets + (
        ("Qo‘shimcha ma’lumotlar", {"fields": ("phone",)}),
    )
