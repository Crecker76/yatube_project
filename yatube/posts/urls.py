from django.urls import path
from . import views
# имя пространста имен
app_name = 'posts'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('group/<slug:slug>/', views.group_posts, name= 'group_list'),
    path('profile/<str:username>/', views.profile, name= 'profile'),
    path('post_detail/<int:post_id>/', views.post_detail, name= 'post_detail'),
    path('create/', views.post_create, name= 'post_create'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='update_post'),
]