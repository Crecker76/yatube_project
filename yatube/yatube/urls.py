from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Пользовательские приложения
    path('', include('posts.urls', namespace='posts')),
    path('auth/', include('users.urls')),
    path('about/', include('about.urls', namespace='about')),
    path('users/', include('users.urls', namespace='users')),
    #Стандартные приложения
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]
