from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# def blog(request):
""" View that brings the blog list page """
# return render(request, 'blog/blog.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'