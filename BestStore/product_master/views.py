from product_master.models import Product
from django.views.generic.detail import DetailView


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_master/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qty'] = range(1, context['object'].quantity + 1)
        product = kwargs['object']
        context['image'] = product.productimages_set.all()
        return context


def add_to_cart(request):
    if request.method == 'POST':
        pass