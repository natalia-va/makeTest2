from django.urls import path, re_path
from . import views

app_name = 'creating_test_app'

urlpatterns = [
    # post views
    path('', views.create_question_model_form),

]