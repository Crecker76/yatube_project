from django.contrib.auth import get_user_model
from django.test import TestCase
from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """ Класс для создания тестовых объектов """


        super().setUpClass()
        # создание объекта пользователя
        cls.user = User.objects.create_user(username='auth')
        # создание объекта группы
        cls.group = Group.objects.create(
            title = 'Тестовая группа',
            slug = 'Тестовый слаг',
            description = 'Тестовое описание',
        )
        # создение тестового поста
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост'
        )
    
    
    def test_models_have_correct_objects_names(self):
        """Проверка что  у модулей корректно работает __str__"""
        post = PostModelTest.post # test object model post
        group = PostModelTest.group # test object model group
        text = post.text # text post
        title = group.title # title group
        self.assertEqual(text, 'Тестовый пост', 'Метод  str модели post возвращает ошибочное значение')
        self.assertEqual(title, 'Тестовая группа', 'Метод  str модели group возвращает ошибочное значение' )

    def test_text_max_length(self):
        """Проверка макисмальной длины возвращаемого значения методом str модели"""
        post = PostModelTest.post
        max_length_text = 15 # максимальная длина возвращаемого значения
        length_text = len(post.text)
        # ПЕРЕПИСАТЬ ДАННОЕ УСЛОВИЕ 
        if length_text < max_length_text:
            var_bool = True # переменная для проверки что длина меньше 15
        else:
            var_bool = False        
        self.assertTrue(var_bool, 'Метод str модели Post возвращает более 15 символов')

