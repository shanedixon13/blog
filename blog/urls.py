from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostEditView,
    PostDeleteView
)

urlpatterns=[
    path('',HomePageView.as_view(), name='index'),
    path('blog/about/',AboutPageView.as_view(), name='about'),
    path('posts/',PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(),name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete')
    ]