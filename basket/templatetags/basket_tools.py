from django import template

""" This enables the subtotal in basket to correctly product the product of price and quanity. """

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
