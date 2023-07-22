from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Question, Answer, User
from .forms import UserLoginForm, QuestionForm, AnswerForm

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Check if the user exists and the password is correct (not recommended in a real-world scenario)
            # For simplicity, we'll assume the user exists and the password is correct.
            return redirect('view_questions')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})

def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'view_questions.html', {'questions': questions})

def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_questions')
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})

def post_answer(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('view_questions')
    else:
        form = AnswerForm()
    return render(request, 'post_answer.html', {'form': form, 'question': question})
