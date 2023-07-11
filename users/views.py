from rest_framework import generics
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsUserOrAdmin
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    ...


class UserView(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOrAdmin]

    serializer_class = UserSerializer
    queryset = User.objects.all()
