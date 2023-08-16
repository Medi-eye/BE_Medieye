from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from accounts.models import Profile
from accounts.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer,UserModelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from core.permissions import IsOwnerOnly
from rest_framework.test import APIClient


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOnly]
    
    def get(self, request, pk, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOnly]
    
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class UserModelView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    