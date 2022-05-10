from django.shortcuts import render
from django.http import HttpResponse
#from httplib2 import Http

# Create your views here.

#функция обработки главной страницы
def index(request):
    template = 'post/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title':title
    }
    return render(request, template, context)

# функция обработки групп
def group_posts(request):
    template = 'post/group_list.html'
    title = 'Тут будет список постов групп'
    context = {
        'title':title
    }
    return render(request, template, context)
