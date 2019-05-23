from django.shortcuts import render
from product_master.models import Category, SubCategory, Product



def home(request):
    return render(request, "master/homepage.html")


def register(request):
    return render(request, "master/register.html")


def login(request):
    return render(request, "master/login.html")


def render_login_form(request):
    return render(request, 'master/login.html')


def cart(request):
    return render(request, 'master/checkout.html')


def product_listings(request):
    if request.method == 'GET':
        try:
            page = int(request.GET.get('page', 1))
        except:
            page = 1
        category = Category.objects.all()
        all_products = Product.objects.all()
        
        prods_per_page = 6

        total_pages = ((abs(len(all_products))-1)//prods_per_page) + 1
        if page < 1:
            page = 1
        elif page > total_pages:
            page = total_pages
        start_index = (page-1) * prods_per_page
        end_index = start_index + prods_per_page
        products = all_products[start_index: end_index]

        info = {
            'category': category, 
            'product': products, 
            'pages': range(1, total_pages+1),
            'current_page': page,
            'prev': f'/products/?page={page-1}' if page != 1 else '#',
            'next': f'/products/?page={page+1}' if page != total_pages else '#',
        }

        return render(request, 'product_master/products.html', context=info)