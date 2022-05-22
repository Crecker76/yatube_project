from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model() #Модель отвечающая за управление пользователями

class Post(models.Model):
    
    text = models.TextField() # поле формата текст
    pub_date = models.DateTimeField(auto_now_add= True) # поле даты создания поста. auth_now_add-для автоматическогоприсваения даты посту
    
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='posts'
        ) # полея для указания ссылки на другую модель(другую таблицу) 
    #on_delete=models.CASCADE обеспечивает связанность данных при удаление пользователя будут удалены все посты 