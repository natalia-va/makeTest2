from django.shortcuts import render, get_object_or_404, redirect
from base_app.models import Question, Test
from .forms import  QuestionModelFormset, TestModelForm
from django.contrib.auth.models import User


def create_question_model_form(request):
    template_name = 'creating_test_app/create_question.html'
    if request.method == 'GET':
        testform = TestModelForm(request.GET or None)
        formset = QuestionModelFormset(queryset=Question.objects.none())
    elif request.method == 'POST':
        testform = TestModelForm(request.POST)
        formset = QuestionModelFormset(request.POST)
        if testform.is_valid() and formset.is_valid():
            test = testform.save()
            test.author = request.user
            test.save()
            for form in formset:
                question = form.save(commit=False)
                question.test = test
                question.save()
            return redirect('base_app:test_list')

    return render(request, template_name, {
        'testform': testform,
        'formset': formset,
    })