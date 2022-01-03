from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('find_username/', views.find_username, name='find_username'),
    path('login/kakao/', views.kakao_login, name="kakao_login"),
    path('login/kakao/callback', views.kakao_login_callback, name="kakao_login_callback"),
]
