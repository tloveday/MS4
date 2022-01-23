from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KLDkbJhG3huTzYi2745itzYf8LU9ct5BTtR6Hx36zuogP3sOhL2oZhsWxhrrO57f0zWa5efHaXMFxcdedL8Gwme004R7qziVH',
        'client_secret': 'test',
    }

    return render(request, template, context)
