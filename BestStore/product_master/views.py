from django.shortcuts import render
from product_master.models import Product
from django.http import JsonResponse
from product_master.models import Product
from django.views.generic.detail import DetailView


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


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_master/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qty'] = range(1, context['object'].quantity + 1)
        product = kwargs['object']
        context['image'] = product.productimages_set.all()
        return context


