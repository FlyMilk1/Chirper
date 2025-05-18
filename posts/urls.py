from django.urls import path
from .views import (
    PostListView,
    post_detail,
    post_create,
    PostDeleteView,
    like_post,
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('post/new/', post_create, name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('like/', like_post, name='like-post'),
]