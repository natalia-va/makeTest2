from django.http import HttpResponse
from django.shortcuts import render
from base_app.models import Test
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    #return render(request, 'account/dashboard.html', {'section': 'dashboard'})
    tests = Test.objects.all()
    return render(request, 'base_app/test_list.html', {'tests': tests})