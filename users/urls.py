from django.urls import path
from .views import register,user_logout,user_login, user_profile, about

urlpatterns = [
    path('register/', register, name='register' ),
    path('logout/', user_logout, name='user_logout' ),
    path('login/', user_login, name='user_login'),
    path('profile/', user_profile, name='user_profile'),
    path('about/', about, name='about'),
]