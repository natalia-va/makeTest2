from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


app_name = 'creating_test_app'

urlpatterns = [

    #path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='auth_app/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]