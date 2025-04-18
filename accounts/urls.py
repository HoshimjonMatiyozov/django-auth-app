from django.urls import path
from .views import RegisterView, MeView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Ro‘yxatdan o‘tish
    path('register/', RegisterView.as_view(), name='register'),

    # Login (JWT access va refresh token qaytaradi)
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # Refresh token orqali yangi access token olish
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Auth bo‘lgan foydalanuvchi ma’lumotlari
    path('me/', MeView.as_view(), name='me'),

    # Logout (refresh tokenni blacklist qiladi)
    path('logout/', LogoutView.as_view(), name='logout'),
]
