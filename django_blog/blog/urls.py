from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, ProfileUpdateView, index
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views


urlpatterns = [
    path('blog/', index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('',PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/delete', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
]
