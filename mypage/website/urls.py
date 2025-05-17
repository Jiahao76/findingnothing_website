from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    path("english/", views.english_front, name="english-front-page"),
    path("japanese/", views.japanese_front, name="japanese-front-page"),
    path("chinese/", views.chinese_front, name="chinese-front-page"),
]