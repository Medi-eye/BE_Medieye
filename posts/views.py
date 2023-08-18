from django.shortcuts import render


from rest_framework.viewsets import generics,ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication

# Create your views here.


from .serializers import MedicineSerializer,ScrapSerializer
from .models import Medicine,Scrap


class MediViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()

'''
유저가 약물들을 즐겨찾기 추가, 리스트, 삭제, 검색 가능한 뷰셋
'''
class ScrapViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ScrapSerializer
    queryset = Scrap.objects.all()

    def get_queryset(self):
        return super(ScrapViewSet,self).get_queryset().filter(user = self.request.user)


