from django.urls import path,include
from rest_framework import routers

from .views import UserListView,UserSignupView,TakenMediViewSet,LoginView,LogoutView,ProfileView,ProfileCreateView,ProfileListView

app_name = 'accounts'

router = routers.SimpleRouter()
router.register(r'taken-medi',TakenMediViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('list/',UserListView.as_view()),
    path('sign-up/',UserSignupView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
    path('login/',LoginView.as_view()),
    path('profile/create/',ProfileCreateView.as_view()),
    path('profile/',ProfileListView.as_view()),
]

