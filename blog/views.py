# Create your views here.
from django.shortcuts import render

from .models import Post
from .forms import PostForm

# Create your views here.


def blog(request):
    """ Returns blog.html """
    return render(request, 'blog/blog.html', {})
