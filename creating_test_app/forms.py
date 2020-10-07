from django import forms

from base_app.models import Question, Test

# forms.py :: part 1

from django import forms
from django.forms import modelformset_factory

class TestModelForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title']
        labels = {
            'title': 'Title of test',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title of test here'
                }
            ),

        }

QuestionModelFormset = modelformset_factory(
    Question,
    fields = ('title','body', 'answer', 'note' ),
    extra=1,
    widgets={
        'title': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter title of question here'
        }
        ),
        'body': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter body of question here'
        }
        ),
        'answer': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter answer here'
        }
        ),
        'note': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter note here'
        }
        )
    }
)



