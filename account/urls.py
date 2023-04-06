from django.urls import path, include
from account.views import ProfileView

urlpatterns = [
    #회원가입
    path('signin/',include('dj_rest_auth.urls')),
    path('signin/signup/',include('dj_rest_auth.registration.urls')),
    path('profile/<int:pk>',ProfileView.as_view()),
]