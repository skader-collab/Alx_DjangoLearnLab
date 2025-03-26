from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, ProfileUpdateView, index

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
]
