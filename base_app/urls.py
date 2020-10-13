from django.urls import path, include
from . import views

app_name = 'base_app'

urlpatterns = [
    # post views
    path('', views.check_auth, name='first_check_auth'),
    path('test/<int:pk>/', views.test_detail, name='test_detail'),
    path('my-tests/', views.test_list, name='test_list'),
    path('creating/', include('creating_test_app.urls')),
    path('delete/<int:pk>/', views.delete_test, name='delete_test'),
    path('account/', include('account_app.urls', namespace='account')),

]