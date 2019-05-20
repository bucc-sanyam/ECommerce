from django.urls import path
from .views import home, register, render_login_form

urlpatterns = [
    path('', home, name="homepage"),
    path('register/', register, name="register"),
    path('login/', render_login_form, name="loginform")
]
