from django.urls import path
from . import views
# имя пространста имен
app_name = 'posts'

urlpatterns = [
    path('', views.index, name= 'index'),
    #path('group/slug:slug/', views.group_posts, name= 'group_list'),
    path('group/group_list/', views.group_posts, name= 'group_list'), # COSTIL
]