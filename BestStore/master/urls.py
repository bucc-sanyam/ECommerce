from django.urls import path, include
from .views import home, register, render_login_form
from product_master.views import ProductDetailView
from .views import (
    home, register, render_login_form, product_listings, checkout
)
from BestStore.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from user_master.views import user_dashboard


urlpatterns = [
    path('', home, name="homepage"),
    path('register/', register, name="register"),
    path('login/', render_login_form, name="loginform"),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('products/', product_listings, name="products"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('checkout/', checkout, name="checkout"),
    path('', include('social_django.urls', namespace='social')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)