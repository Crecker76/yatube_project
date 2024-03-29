# Импортируем необходимые приложения
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


app_name='users' # Пространство имен приложения


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'logout/', 
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'login/', 
        LogoutView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'password_change/', 
        LogoutView.as_view(template_name='users/password_change_form.html'),
        name='password_change_form'
    ),
    path(
        'password_change_done/', 
        LogoutView.as_view(template_name='users/password_change_done.html'),
        name='password_change_done'
    ),
    path(
        'password_reset/', 
        LogoutView.as_view(template_name='users/password_reset_form.html'),
        name='password_reset_form'
    ),
    
]
