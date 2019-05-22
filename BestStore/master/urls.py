from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from .views import home, register, render_login_form
from product_master.views import ProductDetailView
from BestStore.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('', home, name="homepage"),
    path('register', register, name="register"),
    path('login/', render_login_form, name="loginform"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('', include('social_django.urls', namespace='social')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)