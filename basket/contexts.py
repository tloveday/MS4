

def basket_contents(request):

    basket_items = []
    total = 0
    products_count = 0

    grand_total = total

    context = {
        'basket_items': basket_items,
        'total': total,
        'products_count': products_count,
        'grand_total': grand_total,
    }

    return context
