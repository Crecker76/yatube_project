from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms
from ..models import Post, Group

User = get_user_model()



class PostPagesTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.user = User.objects.create_user(username='StasVlasov')
       
        # создание объекта группы
        cls.group = Group.objects.create(
            title = 'Тестовая группа',
            slug = 'test_slug',
            description = 'Тестовое описание',
        )
        # создение тестового поста
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
            pk = 156,
            group = cls.group
                    
        )
        

    def setUp(self):
        # Неавторизированный пользователь
        self.guest_client = Client()
        # создаем объект пользователя        
        # Второй клиент
        self.authorized_client = Client()
        # Авторизуем пользователя
        self.authorized_client.force_login( PostPagesTest.user)

    def test_pages_user_correct_template(self):
        #URl адреса используют соответствующие шаблоны
        template_pages_names = {
            'posts/index.html': reverse('posts:index'),
            'posts/group_list.html': reverse('posts:group_list', kwargs={'slug': 'test_slug'}),          
            'posts/profile.html': reverse('posts:profile', kwargs={'username': 'StasVlasov'}),
            # Запилить данные ссылки
            #'posts/create_posts.html': reverce(posts:post_edit)
            #'posts/create_posts.html': reverce(posts:create_post)
            'posts/post_detail.html': reverse('posts:post_detail', kwargs={'post_id': 156})
        }

        # проверка что возвращается правильный шаблон
        for template, reverse_name in template_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.guest_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    def test_home_page_show_correct_context(self):
        """ Шаблон сформирован с правильным контекстом  posts/index.html"""
        response = self.authorized_client.get(reverse('posts:index'))
        first_object = response.context['page_obj'][0]
        posts_text_0 = first_object.text
        posts_author_0 = first_object.author   
        self.assertEqual(posts_text_0, 'Тестовый пост')
        self.assertEqual(posts_author_0, PostPagesTest.user)

    
   
    def test_group_list_page_show_correct_context(self):
        # Проверка правильности контектса  group_list
        responce = self.authorized_client.get(reverse('posts:group_list', kwargs={'slug': 'test_slug'}))
        first_object = responce.context['page_obj'][0]
        posts_text = first_object.text
        posts_author = first_object.author
        self.assertEqual(posts_text, 'Тестовый пост')
        self.assertEqual(posts_author, PostPagesTest.user )
        
    

    def test_profile_page_show_correct_context(self):        
        responce = self.authorized_client.get(reverse('posts:profile', kwargs={'username': 'StasVlasov'}))
        first_object = responce.context['page_obj'][0]
        self.assertEqual(first_object.text, 'Тестовый пост')
        self.assertEqual(first_object.author, PostPagesTest.user)
    
    
    """
    def test_post_detail_page_show_correct_context(self):
        responce = self.authorized_client.get('posts:post_detail', kwargs={'post_id': int(156)})
        print(responce.status_code)
        
        print(dir(responce.context) )  
        print(responce.render_context())    
        print(responce.status_code)
    """
    def test_create_post_page_show_correct_context(self):
        #  проверка создания нового поста
        responce = self.authorized_client.get(reverse('posts:post_create'))
        form_fields = {            
            # При создании формы поля модели типа TextField 
            # преобразуются в CharField с виджетом forms.Textarea           
            'text': forms.fields.CharField,
            'group': forms.models.ModelChoiceField,
        }
        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = responce.context.get('form').fields.get(value)
                # Проверяет, что поле формы является экземпляром
                # указанного класса
                self.assertIsInstance(form_field, expected)
    
    def test_update_post_page_show_correct_context(self):
        # проверка страницы редактирования поста
        responce = self.authorized_client.get(reverse('posts:update_post', kwargs={'post_id': int(156)}))
        
        form_fields = {            
            # При создании формы поля модели типа TextField 
            # преобразуются в CharField с виджетом forms.Textarea           
            'text': forms.fields.CharField,
            'group': forms.models.ModelChoiceField,
        }
        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = responce.context.get('form').fields.get(value)
                # Проверяет, что поле формы является экземпляром
                # указанного класса
                self.assertIsInstance(form_field, expected)
    
        

class PaginatorViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
         #создение тестового поста
        cls.user = User.objects.create_user(username='DimanK')
         #создание объекта группы
        cls.group = Group.objects.create(
            title = 'Тестовая группа',
            slug = 'test_slug',
            description = 'Тестовое описание',
        )
        
        Post.objects.create(
            text='Тестовый пост 1',
            author=cls.user,
            group = cls.group,                  
        )
        Post.objects.create(
            text='Тестовый пост 2',
            author=cls.user,
            group = cls.group,                   
        )
        Post.objects.create(
            text='Тестовый пост 3',
            author=cls.user,
            group = cls.group,                    
        )
        Post.objects.create(
            text='Тестовый пост 4',
            author=cls.user,
            group = cls.group,                  
        )
        Post.objects.create(
            text='Тестовый пост 5',
            author=cls.user,
            group = cls.group,                    
        )
        Post.objects.create(
            text='Тестовый пост 6',
            author=cls.user,
            group = cls.group,                    
        )
        Post.objects.create(
            text='Тестовый пост 7',
            author=cls.user,
            group = cls.group,                  
        )
        Post.objects.create(
            text='Тестовый пост 8',
            author=cls.user,
            group = cls.group,                    
        )
        Post.objects.create(
            text='Тестовый пост 9',
            author=cls.user,
            group = cls.group,                    
        )
        Post.objects.create(
            text='Тестовый пост 10',
            author=cls.user,
            group = cls.group,                 
        )
        Post.objects.create(
            text='Тестовый пост 11',
            author=cls.user,
            group = cls.group,                 
        )
        Post.objects.create(
            text='Тестовый пост 12',
            author=cls.user,
            group = cls.group,                
        )
        Post.objects.create(
            text='Тестовый пост 13',
            author=cls.user,
            group = cls.group,                 
        )
        
    def setUp(self):
        # Неавторизированный пользователь
        self.guest_client = Client()
        # создаем объект пользователя        
        # Второй клиент
        self.authorized_client = Client()
        # Авторизуем пользователя
        self.authorized_client.force_login( PaginatorViewsTest.user)

    def test_home_page_contains_ten_records(self):
        responce = self.authorized_client.get(reverse('posts:index'))
        self.assertEqual(len(responce.context['page_obj']), 10) # Выводится по 10 постов на странице
    
    def test_two_home_page_contains_three_records(self):
        responce = self.authorized_client.get(reverse('posts:index') + '?page=2')
        self.assertEqual(len(responce.context['page_obj']), 3) # Выводится по 10 постов на странице
    
    def test_group_list_contains_ten_records(self):
        responce = self.authorized_client.get(reverse('posts:group_list', kwargs={'slug': 'test_slug'}))
        self.assertEqual(len(responce.context['page_obj']), 10) # Выводится по 3 постов на странице
    
    def test_two_group_list_page_contains_three_records(self):
        responce = self.authorized_client.get(reverse('posts:group_list', kwargs={'slug': 'test_slug'}) + '?page=2')
        self.assertEqual(len(responce.context['page_obj']), 3) # Выводится по 3 постов на странице

    def test_profile_contains_ten_records(self):
        responce = self.authorized_client.get(reverse('posts:profile', kwargs={'username': 'DimanK'}))
        self.assertEqual(len(responce.context['page_obj']), 10) # Выводится по 3 постов на странице
    
    def test_profile_list_page_contains_three_records(self):
        responce = self.authorized_client.get(reverse('posts:profile', kwargs={'username': 'DimanK'}) + '?page=2')
        self.assertEqual(len(responce.context['page_obj']), 3) # Выводится по 3 постов на странице

    def test_additional_to_enter_posts_in_index(self):
        #  проверка что при налчиии группы у поста он отображается на главной странице
        response = self.authorized_client.get(reverse('posts:index'))
        first_object = response.context['page_obj']
        for one_post in first_object:            
            # ругается что приходят разные значения
            self.assertEqual(str(one_post.group), str('Тестовая г'))

    def test_additional_to_enter_posts_in_group_list(self):
        #  проверка на отображение всех постав на странице группы
        responce = self.authorized_client.get(reverse('posts:group_list', kwargs={'slug': 'test_slug'}))
        first_object = responce.context['page_obj']        
        for one_post in first_object:            
            self.assertEqual(one_post.group, PaginatorViewsTest.group)
            
            
    def test_additional_to_enter_posts_in_profile(self):
        responce = responce = self.authorized_client.get(reverse('posts:profile', kwargs={'username': 'DimanK'}))
        first_object = responce.context['page_obj']
        for one_post in first_object:    
            self.assertEqual(one_post.author, PaginatorViewsTest.user)
            


