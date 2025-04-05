from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser

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

