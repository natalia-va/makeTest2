from django.shortcuts import render, get_object_or_404
from .models import Question, Test



def test_list(request):
    tests = Test.objects.all()
    return render(request, 'base_app/test_list.html', {'tests': tests})

def test_detail(request, pk):
    test = Test.objects.get(id=pk)
    questions = Question.objects.filter(test=test)
    return render(request, 'base_app/test_detail.html', {'questions': questions})