from django.contrib import admin
from .models import Test, Question

class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'link')
    list_filter = ['author']
    search_fields = ['title']

admin.site.register(Test, TestAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'number')
    list_filter = ['test']
    search_fields = ['test']

admin.site.register(Question, QuestionAdmin)