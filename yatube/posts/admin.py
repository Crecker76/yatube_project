from django.contrib import admin

# Register your models here.
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('text', 'pub_date', 'author', 'group')
    # Для смены группы непосредственно в поле
    list_editable = ('group',) 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',) 

admin.site.register(Post,PostAdmin) # добавление модели пост в панель админа
admin.site.register(Group)