from django.shortcuts import render, get_object_or_404
from .models import Post, Group

<<<<<<< HEAD
=======
NUM_OF_POSTS: int = 10 # количество постов для вывода на страницу
>>>>>>> 570208c2d90b232d95288c6f1f2794164c308f0e

# функция обработки главной страницы
def index(request):
    template = 'posts/index.html'
<<<<<<< HEAD
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    # последние 10 постов из базы данных
    context = {
        'title': title,
=======
    #title = 'Это главная страница проекта Yatube'
    posts = Post.objects.select_related('author', 'group')[:NUM_OF_POSTS] # последние количество постов из базы данных
    context = {        
        'posts':posts,
    }
    return render(request, template, context)

# функция обработки групп
def group_posts(request, slug):  
    template = 'posts/group_list.html'
    #title = 'Тут будет список постов групп'
    group = get_object_or_404(Group, slug=slug)
    #posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUM_OF_POSTS]
    posts = group.groups.all()[:NUM_OF_POSTS]# group-object, groups-related name models, all()- all posts group
    context = {        
        'group': group,
>>>>>>> 570208c2d90b232d95288c6f1f2794164c308f0e
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
