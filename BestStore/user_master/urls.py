from django.urls import path
from .views import user_login
from .views import logout_view
from .views import register_user
from .views import user_dashboard
from .views import verify_user_email
from .views import UpdateUserProfile
from .views import DeleteUserProfile

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', user_login, name='user_login'),
    path('register/', register_user, name='register_post'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('verify/<str:token>/', verify_user_email, name='user_verify'),
    path('profile_delete/<int:pk>/', DeleteUserProfile.as_view(), name='delete_profile'),
    path('profile_update/<int:pk>/', UpdateUserProfile.as_view(success_url='/api/user/dashboard/'),
         name='update_profile'),
]
