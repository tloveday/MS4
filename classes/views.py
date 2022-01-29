from django.shortcuts import render


def tigers(request):
    """ View that brings the basket contents page """
    return render(request, 'classes/tigers.html')


def juniors(request):
    """ View that brings the basket contents page """
    return render(request, 'classes/juniors.html')


def seniors(request):
    """ View that brings the basket contents page """
    return render(request, 'classes/seniors.html')


def ladies(request):
    """ View that brings the basket contents page """
    return render(request, 'classes/ladies.html')
