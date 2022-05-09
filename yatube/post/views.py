from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#функция обработки главной страницы
def index(request):
    return HttpResponse('Main paige')

# функция обработки групп
def group_posts(request, slug):
    return HttpResponse(f'Group_post {slug}')
