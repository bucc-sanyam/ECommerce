from django.urls import path, include
from .views import home, register, login, logout
urlpatterns = [
    path('', home, name="homepage"),
    path('register', register, name="register"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('', include('social_django.urls', namespace='social')),
]
