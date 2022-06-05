<<<<<<< HEAD
from tokenize import group
=======
>>>>>>> 570208c2d90b232d95288c6f1f2794164c308f0e
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Пользовательские приложения
    path('', include('posts.urls', namespace='posts')),
    path('auth/', include('users.urls')),
    #Стандартные приложения
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]
