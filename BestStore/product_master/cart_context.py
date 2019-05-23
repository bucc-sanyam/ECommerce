from .models import Product


def add_session_cart(request):
    total_qty = 0
    total_price = 0 
    cart = request.session.get('cart', False)
    if cart:
        for details in cart:
            total_qty += details['qty']
            price = Product.objects.get(pk=details['pk']).price
            total_price += price * details['qty']

    return {'total_qty': total_qty, 'total_price': total_price}