from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

from .serializers import serializers
# from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

class RegisterView(APIView):
    @extend_schema(
            request=RegisterSerializer,
            responses={200: 'Main list'}
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        validated_data = serializer.validated_data
        if serializer.is_valid():
            if User.objects.filter(username=validated_data['username']).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
            )
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         email = request.data.get('email')

#         if User.objects.filter(username=username).exists():
#             return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

#         user = User.objects.create_user(username=username, password=password, email=email)
#         return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    return Response({
        "id": request.user.id,
        "username": request.user.username,
        "email": request.user.email
    })
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })