from django.urls import path
from .views import PostList,PostCreate,PostDetail,PostUpdate,PostDelete
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post_create/', PostCreate.as_view(), name='post_create'),
    path('post_detail/<int:id>/', PostDetail.as_view(), name='post_detail'),
    path('post_update/<int:id>/', PostUpdate.as_view(), name='post_update'),
    path('post_delete/<int:id>/', PostDelete.as_view(), name='post_delete'),
  
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)