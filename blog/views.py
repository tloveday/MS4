from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'


class AddPost(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'
    
