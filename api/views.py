from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import response
from .serializers import UserRegistrationSerializer, ProductSerializer
from .models import Product
from .permissions import IsSuperAdmin, IsAdmin  # Import custom permissions

User = get_user_model()

# View for the landing page


def landing_page(request):
    return render(request, 'index.html')  # Render the landing page template

# View for user registration


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

# View for user login


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return response.Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return response.Response({'error': 'Invalid credentials'}, status=400)

# View for managing users (only accessible by Super Admin)


class UserManagementView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsSuperAdmin]  # Only Super Admin can access

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # Ensure the user is authenticated
            users = self.get_queryset()
            serializer = UserRegistrationSerializer(users, many=True)
            return response.Response(serializer.data)
        return response.Response({'error': 'Unauthorized'}, status=401)

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=201)
        return response.Response(serializer.errors, status=400)
