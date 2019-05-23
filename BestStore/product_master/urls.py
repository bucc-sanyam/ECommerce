from django.urls import path
from .views import cart_add, cart_empty

urlpatterns = [
    path('cart/add/<int:pk>/', cart_add, name='cart-add'),
    path('cart/empty/', cart_empty, name='cart-empty-all'),
    path('cart/empty/<int:pk>/', cart_empty, name='cart-empty')
]
