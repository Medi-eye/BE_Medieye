from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser
from rest_framework.response import Response


from rest_framework.authentication import TokenAuthentication
from rest_framework.test import APIClient
from core.permissions import IsOwnerOnly

from .serializers import (UserModelSerializer,UserSignupSerializer,
    UserTakenMediSerializer,ProfileSerializer,LoginSerializer,
    )
from .models import User, UserTakenMedi,Profile

# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer

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
    
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class ProfileCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def get_queryset(self):
        return super(ProfileView,self).get_queryset().filter(user = self.request.user)
    
class ProfileListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()




class UserModelView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    





# 유저의 복용약물을 추가, 리스트, 삭제, 수정할 수 있는 뷰셋
class TakenMediViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = UserTakenMedi.objects.all()
    serializer_class = UserTakenMediSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user.email)
        return super(TakenMediViewSet, self).get_queryset().filter(user = self.request.user)
