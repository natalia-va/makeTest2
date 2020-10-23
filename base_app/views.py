from django.shortcuts import render, get_object_or_404
from .models import Question, Test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseNotFound



def check_auth(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('my-tests/')
    else:
        return HttpResponseRedirect('account/')

def test_list(request):
    tests = Test.objects.filter(author=request.user)
    if (tests):
        return render(request, 'base_app/tests_list.html', {'tests': tests})
    else:
        return render(request, 'base_app/tests_list.html')


def test_detail(request, pk):
    test = Test.objects.get(id=pk)
    questions = Question.objects.filter(test=test)
    return render(request, 'base_app/test_detail.html', {'questions': questions})

def delete_test(request, pk):
    try:
        Test.objects.get(id=pk).delete()
        return HttpResponseRedirect("/")
    except Test.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")