from django.views.generic import CreateView #  Импорт для создания наследника
from django.urls import reverse_lazy # позволяет получить URL по параметрам функкиц path
from .forms import CreationForm # class From


class SignUp(CreateView):
    form_class = CreationForm # Из какого класса взята форма
    # После успешной регистрации перенаправляем пользователя на главную
    success_url = reverse_lazy('posts:index') # куда перенаправлять после успешной регистрации
    # Куда будет передана переменная form с объектом HTML форм, работа похожа на функцию render
    template_name = 'users/signup.html' 
