from django.urls import path
from .views import BlogView, PostView, AddPost

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('add_post', AddPost.as_view(), name='add_post'),
]
