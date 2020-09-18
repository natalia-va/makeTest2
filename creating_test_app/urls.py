from django.urls import path
from . import views

app_name = 'creating_test_app'

urlpatterns = [
    # post views
    path('', views.creating_test),

]