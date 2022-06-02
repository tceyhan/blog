from django.urls import path
from .views import register,user_logout,user_login, user_profile, about
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', register, name='register' ),
    path('logout/', user_logout, name='user_logout' ),
    path('login/', user_login, name='user_login'),
    path('profile/', user_profile, name='user_profile'),
    path('about/', about, name='about'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)