from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from ..models import Post, Group


User = get_user_model()


class StaticURLTests(TestCase):

    def setUp(self):
        # Неавторизированный пользователь
        self.guest_client = Client()
        

    def test_home_url_exists_at_desired_location(self):
        """Проверка доступности главной страницы"""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200, f'Ошибка возврата главной страницы код ответа {response.status_code}')

