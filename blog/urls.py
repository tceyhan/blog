from . import views
from django.urls import path
from .views import PostList,PostCreate,PostDetail,PostUpdate,PostDelete
from .feeds import LatestPostsFeed
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post_create/', PostCreate.as_view(), name='post_create'),
    path('post_detail/<int:id>/', PostDetail.as_view() , name='post_detail'),    
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]