from django.urls import path
from .views import RegisterView, MeView
from .views import LogoutView
from .views import me
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('me/', MeView.as_view(), name='me'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
