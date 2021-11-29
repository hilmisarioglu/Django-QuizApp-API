from django.contrib import admin
from .models import Category, Quiz, Question, Answer
import nested_admin
# Register your models here.

class AnswerTabularInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 5 # Add another answer 5 tane daha ekler.
    max_numbers = 8 # Add another answer max 8 e kadar izin verir

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