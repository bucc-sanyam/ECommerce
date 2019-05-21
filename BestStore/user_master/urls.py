from django.urls import path
from .views import register_user, user_login, verify_user

urlpatterns = [
    path('register/', register_user, name='register_post'),
    path('login/', user_login, name='user_login'),
    path('verify/<str:token>/', verify_user, name='user_verify')
]
