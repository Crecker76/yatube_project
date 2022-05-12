from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post) # добавление модели пост в панель админа