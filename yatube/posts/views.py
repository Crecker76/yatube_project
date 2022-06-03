from turtle import title
from django.shortcuts import render, get_object_or_404

from .models import Post, Group

# Create your views here.

#функция обработки главной страницы
def index(request):
    title = 'Последние обнолвения на сайте'
    posts = Post.objects.order_by('-pub_date')[:10] # последние 10 постов из базы данных
    context = {
        'title':title,
        'posts':posts,
    }
    return render(request, 'posts/index.html', context)

# функция обработки групп
def group_posts(request,slug):  
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


    