from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ View to Show All products, including sorting and search quries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)