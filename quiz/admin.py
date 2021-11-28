from django.contrib import admin
import nested_admin
from .models import Category, Quiz, Question, Answer
# Register your models here.

class AnswerTabularInline(nested_admin.NestedTabularInline):
    model = Answer

class QuestionTabularInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerTabularInline]

class QuizTabularInline(nested_admin.NestedTabularInline):
    model = Quiz
    inlines = [QuestionTabularInline]

class CategoryAdmin(nested_admin.NestedModelAdmin):
    model = Category
    inlines = [QuizTabularInline]


admin.site.register(Category,CategoryAdmin)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)