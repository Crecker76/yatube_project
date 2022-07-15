"""
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from posts.models import Post, Group
from django.contrib.auth import get_user_model

User = get_user_model()

class PostCreateFormTest(TestCase):
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
        self.authorized_client.force_login(PostCreateFormTest.user)

    def test_create_post(self):
        posts_count = Post.objects.count()
        form_data = {
            'text': 'Тестовый пост для создания через форму',
            'group': PostCreateFormTest.group
            # группу можно не добавлять
        }

        responce = self.authorized_client.post(
            reverse('posts:post_create'),
            date = form_data,
            follow = True
        )
        print(responce)
        #self.assertRedirects(responce, reverse('posts:profile', kwargs={'username': 'StasVlasov'}))
        #self.assertEqual(Post.objects.count(), posts_count +1, 'Новый тестовый пост не был создан через форму post_create')
"""

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from posts.models import Post, Group
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()

class PostFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='StasLubar')
        cls.group = Group.objects.create(
            title='Тестовый титул',
            slug='test-slug',
        )
        cls.post = Post.objects.create(
            pk=10,
            text='Тестовый текст',
            group=cls.group,
            author=User.objects.get(username='StasLubar')
        )
    def setUp(self):
        self.user = PostFormTests.user
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_create_post(self):
        
        post_count = Post.objects.count()  
        form_data = {
            'text': 'Тестовый текст',
            'group': self.group.pk,
        }
        response = self.authorized_client.post(
            reverse('posts:post_create'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, reverse('posts:profile', args=(self.user.username,)))
        self.assertEqual(Post.objects.count(), post_count+1)

    
    def test_edit_post(self):
        
        group_field_new = self.group.id
        edit_post_var = Post.objects.get(id=self.post.id)
        form_data = {
            'text': 'Тестовый текст',
            'group': group_field_new,
        }
        response = self.authorized_client.post(
            reverse(
                'posts:update_post',
                kwargs={
                    'post_id': self.post.pk
                }

            ),
            data=form_data,
            follow=True
        )
        self.assertRedirects(
            response,
            reverse(
                'posts:post_detail',
                kwargs={
                    'post_id': self.post.pk
                }
            )
        )
        self.assertEqual(edit_post_var.text, form_data['text'])
        self.assertEqual(edit_post_var.author, self.post.author)
    
