from django.shortcuts import render, get_object_or_404
from base_app.models import Question, Test
from .forms import QuestionForm


def creating_test(request):
    form = QuestionForm()
    return render(request, 'creating_test_app/creating_test.html', {'form': form})

def update_list_questions(request):
    return render(request, 'creating_test_app/creating_test.html')