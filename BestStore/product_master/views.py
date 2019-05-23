from django.shortcuts import render
from product_master.models import Product
from django.http import JsonResponse


def manage_cart(request, pk):
    if request.method == 'GET':
        sess = request.session
        qty = request.GET.get('qty', 1)

        sess['cart_qty'] = sess.get('cart_qty', 0) + qty
        sess['cart'] = sess.get('cart', list())

        already_in_cart = False
        for prod in sess['cart']:
            if prod['pk'] == pk:
                already_in_cart = True
                prod['qty'] += qty
        if not already_in_cart:
            sess['cart'].append({'pk': pk, 'qty': qty})

        return JsonResponse({'success': True})

