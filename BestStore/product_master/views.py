from datetime import timezone
from django.shortcuts import render
from django.views.generic.detail import DetailView
from product_master.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_master/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qty'] = range(1, context['object'].quantity + 1)
        product = kwargs['object']
        context['image'] = product.productimages_set.all()
        return context