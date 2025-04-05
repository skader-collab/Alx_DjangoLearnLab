from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# If you want to customize the admin interface further for your custom fields:
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add custom fields to the display, fieldsets, etc.
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'follower_count', 'following_count')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Profile', {'fields': ('bio', 'profile_picture', 'followers')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Profile', {'fields': ('bio', 'profile_picture')}),
    )

    filter_horizontal = ('followers',) 

admin.site.register(CustomUser, CustomUserAdmin)

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, # Use settings.AUTH_USER_MODEL
        related_name='following',
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.username


    @property
    def follower_count(self):
        return self.followers.count()

    @property
    def following_count(self):
        return self.following.count()