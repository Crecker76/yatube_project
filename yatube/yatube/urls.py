from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'

# Данная запись позволяет обращаться 
# к файлам в дерриктории при режиме отладки указанной в 
# в MEDIA_ROOT по имени, через префикс MEDIA_URL
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
