from . import views
from django.urls import path
from .views import PostList,PostCreate,post_detail,PostUpdate,PostDelete
from .feeds import LatestPostsFeed
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post_create/', PostCreate.as_view(), name='post_create'),
    path('post_detail/<int:id>/', post_detail, name='post_detail'),
    path('post_update/<int:id>/', PostUpdate.as_view(), name='post_update'),
    path('post_delete/<int:id>/', PostDelete.as_view(), name='post_delete'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]