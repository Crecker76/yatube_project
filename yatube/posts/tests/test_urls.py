from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from ..models import Post, Group


User = get_user_model()


class StaticURLTests(TestCase):
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
            pk = 84,
            group = cls.group
                    
        )
        

    def setUp(self):
        # Неавторизированный пользователь
        self.guest_client = Client()
        # создаем объект пользователя        
        # Второй клиент
        self.authorized_client = Client()
        # Авторизуем пользователя
        self.authorized_client.force_login(StaticURLTests.user)
        

    def test_urls_availability_page(self):
        # Тест достпуности страниц для всех
         
        url_names = {
            '/': 200,
            f'/group/{StaticURLTests.group.slug}/': 200,
            f'/profile/{StaticURLTests.user.username}/':200,
            f'/post_detail/{StaticURLTests.post.pk}/':200,
            '/unixisting_page':404,
        }

        for address, st_code in url_names.items():
            with self.subTest(st_code=st_code):
                response = self.guest_client.get(address)
                self.assertEqual(response.status_code, st_code)

    
    def test_urls_availsbility_page_post_to_the_author(self):
        # Проверка доступности страницы редактирования поста автору
        response = self.authorized_client.get('/posts/84/edit/')
        print(StaticURLTests.post.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_urls_availability_page_create_authorized_user(self):
        # Доступность страницы создания поста авторизованному пользователя
        response = self.authorized_client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_urls_uses_correct_template(self):
        # Проверка возвращаемых шаблонов адресами
        template_url_names = {
            'posts/index.html': '/',
            'posts/group_list.html': '/group/test_slug/',
            'posts/profile.html': f'/profile/{StaticURLTests.user.username}/',
            'posts/post_detail.html': f'/post_detail/{StaticURLTests.post.pk}/',
            'posts/create_post.html': '/posts/84/edit/',
        }

        for template, address in template_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)

    def test_urls_page_create_post_correct_template(self):
        # функция проверки шаблона страницы создания поста
        response = self.authorized_client.get('/create/')
        self.assertTemplateUsed(response, 'posts/create_post.html')
