from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('questions/', views.view_questions, name='view_questions'),
    path('post-question/', views.post_question, name='post_question'),
    path('post-answer/<int:question_id>/', views.post_answer, name='post_answer'),
]
