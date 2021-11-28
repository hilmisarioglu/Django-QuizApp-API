from django.contrib import admin
import nested_admin
from .models import Category, Quiz, Question, Answer
# Register your models here.

class AnswerTabularInline(nested_admin.NestedTabularInline):
    model = Answer

class QuestionTabularInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerTabularInline]

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionTabularInline]



admin.site.register(Category)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)