from django import forms

from base_app.models import Question

class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['class'] = 'some_class'
    class Meta:
        model = Question
        fields = ('body', 'answer', 'note')