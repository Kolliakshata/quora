from django import forms
from .models import Question, Answer, User

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
