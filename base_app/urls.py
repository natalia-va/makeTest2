from django.urls import path, include
from . import views

app_name = 'base_app'

urlpatterns = [
    # post views
    path('test/<int:pk>/', views.test_detail, name='test_detail'),
    path('', views.test_list, name='test_list'),
    path('creating/', include('creating_test_app.urls')),
    path('delete/<int:pk>/', views.delete_test, name='delete_test'),
    path('auth/', include('auth_app.urls', namespace='auth')),

]