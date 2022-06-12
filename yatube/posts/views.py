from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group, User

NUM_OF_POSTS: int = 10 # количество постов для вывода на страницу

#функция обработки главной страницы
def index(request):
    template = 'posts/index.html'
    #posts = Post.objects.select_related('author', 'group')[:NUM_OF_POSTS] # последние количество постов из базы данных
    #Запрос к базе данных 
    post_list = Post.objects.all()
    #Создание погинатора с параметрами по 10 на странице
    paginator = Paginator(post_list, NUM_OF_POSTS)
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    context = {        
        'page_obj': page_obj
    }
    return render(request, template, context)

# функция обработки групп
def group_posts(request, slug):  
    template = 'posts/group_list.html'    
    group = get_object_or_404(Group, slug=slug)
    #posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUM_OF_POSTS]
    posts = group.groups.all()[:NUM_OF_POSTS]# group-object, groups-related name models, all()- all posts group
    context = {        
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)

def profile(request, username):
    # Код запроса к модели и создание словоря контекста
   
    
    template = 'posts/profile.html'
    user = get_object_or_404(User, username=username)
    post_list = user.posts.all()
    amount_posts = post_list.count() # amount posts user
    paginator = Paginator(post_list, NUM_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'page_obj': page_obj,
        'amount_posts': amount_posts,
    }
    return render(request, template , context)
    

def post_detail(request, post_id):
    # код запроса инофрмации о конкретном посте


    template = 'posts/post_detail.html'
    post = Post.objects.get(pk=post_id)    
    amount_posts_author = post.author.posts.all().count()
    context = {
        'post': post,
        'amount_posts_author': amount_posts_author,
    }
    return render(request, template , context)
    

    