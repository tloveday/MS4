from django.shortcuts import render


def blog(request):
    """ View that brings the blog list page """
    return render(request, 'blog/blog.html', {})
