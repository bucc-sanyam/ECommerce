from django.urls import path
from .views import manage_cart

urlpatterns = [
    path('cart/add/<int:pk>/', manage_cart, name='update-cart')
]
