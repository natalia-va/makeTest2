from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


app_name = 'creating_test_app'

urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('', views.reg_auth),
]