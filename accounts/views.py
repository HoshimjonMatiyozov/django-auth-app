from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiExample
from django.contrib.auth import get_user_model
from .serializers import LoginSerializer
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema
from .serializers import LogoutSerializer

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    @extend_schema(
        request=RegisterSerializer,
        responses={201: RegisterSerializer},
        summary="Foydalanuvchini ro'yxatdan o'tkazish"
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Get current user info",
        operation_description="Returns details of the currently authenticated user.",
        responses={200: UserSerializer}
    )
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=LogoutSerializer,
        operation_summary="Logout user (Blacklist refresh token)",
        responses={204: "No Content"}
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            token = RefreshToken(serializer.validated_data['refresh'])
            token.blacklist()
        except Exception as e:
            return Response({"error": "Invalid token or already blacklisted"}, status=400)

        return Response(status=204)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginSerializer

    @extend_schema(
        summary="Login (JWT access va refresh token olish)",
        request=LoginSerializer,
        tags=["Authentication"],
        responses={
            200: OpenApiExample(
                "Tokenlar",
                value={
                    "refresh": "your_refresh_token_here",
                    "access": "your_access_token_here"
                }
            ),
            401: OpenApiExample(
                "Noto‘g‘ri login",
                value={"detail": "No active account found with the given credentials"}
            )
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
