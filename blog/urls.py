from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:post_id>/', views.blog_post, name='post'),
    path('addpost/', views.add_post, name='add_post'),
]
