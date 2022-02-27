# Create your views here.
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.


def blog(request):
    """ Returns blog.html """
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def blog_post(request, post_id):
    """ Returns post.html """
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)


def add_post(request):
    # Superuser Only
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You do not have permission to do that')
        return redirect(reverse('blog'))
    # Add Blog Post
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save()
            messages.success(request, 'Blog post successfully published')
            return redirect(reverse('post', args=[post.id]))
        else:
            messages.error(request, 'Failed to add post.')
    else:
        post_form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'post_form': post_form,
        'on_profile_page': True
    }

    return render(request, template, context)
