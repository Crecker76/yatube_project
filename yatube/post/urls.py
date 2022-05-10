from django.urls import path
from . import views
# имя пространста имен
app_name = 'post'

urlpatterns = [
    path('', views.index, name= 'index'),
    #path('group/slug:slug/', views.group_posts),
    path('group/group_list/', views.group_posts, name= 'group_list'), # COSTIL
]