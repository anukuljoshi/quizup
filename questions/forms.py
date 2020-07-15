from django import forms

from .models import Question, Answer

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question'
        ]
        widgets = {
            'question' : forms.Textarea(attrs={'rows':3})
        }

class AnswerCreateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'answer'
        ]
        widgets = {
            'answer' : forms.Textarea(attrs={'rows': 3})
        }