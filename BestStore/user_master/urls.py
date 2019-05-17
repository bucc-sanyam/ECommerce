from django.urls import path
from .views import testpost
urlpatterns = [
    path('register/', testpost, name='register_post'),

]
