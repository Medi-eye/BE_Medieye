from django.urls import path
from rest_framework import routers
from accounts.views import RegisterView, LoginView, ProfileView,UserModelView


urlpatterns = [
    path('signup/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('list/',UserModelView.as_view()),
    
    path('profile/<int:pk>', ProfileView.as_view()),
]