from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from basket.contexts import basket_contents
from products.models import Product

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }
        order_form = OrderForm(form_data)
        """ Save Valid order form """
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by-size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                        order_line_item.save()
                except product.DoesNotExist:
                    """ Item not in Database """
                    messages.error(request, (
                        "One of the items in your basket wasn't found!"
                        "Please check with your instructor.")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            """ If user saves infor to profile """
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            """ If form is not valid """
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        """ If there is nothing in basket """
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "Your basket is empty")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
            )

        print(intent)

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing - Did you set it')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ Successful Checkout Page """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your Order Number is {order_number}. \
        A Confirmation Email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
