from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# функция обработки главной страницы
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    # последние 10 постов из базы данных
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


# функция обработки групп
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Тут будет список постов групп'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
