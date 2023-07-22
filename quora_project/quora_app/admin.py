from django.contrib import admin
from .models import Question, Answer, User
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'content', 'date_created', 'likes')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
