# Create your views here.
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_post(request):
    # Superuser Only
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You do not have permission to do that')
        return redirect(reverse('blog'))
    # Add Blog Post
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
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


@login_required
def edit_post(request, post_id):
    # Superuser Access Only
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You do not have permission to do that')
        return redirect(reverse('blog'))
    # Edit Blog Post
    # Prefill Form with Info from DB
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Post successfully updated')
            return redirect(reverse('post', args=[post.id]))
        else:
            messages.error(request,
                           'Error - Please check form is valid and try again.')
    else:
        post_form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'post_form': post_form,
        'post': post,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Superuser Access Only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, You do not have permission to do that')
        return redirect(reverse('blog'))
    # Delete Post 
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Your post was deleted')
    return redirect(reverse('blog'))
