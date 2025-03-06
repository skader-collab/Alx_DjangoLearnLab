from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

    def __str__(self):
        return self.title



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")

admin.site.register(CustomUser, CustomUserAdmin)

# Create groups
editors_group, _ = Group.objects.get_or_create(name="Editors")
viewers_group, _ = Group.objects.get_or_create(name="Viewers")
admins_group, _ = Group.objects.get_or_create(name="Admins")

# Get permissions
content_type = ContentType.objects.get_for_model(Book)
permissions = Permission.objects.filter(content_type=content_type)

# Assign permissions
editors_group.permissions.set(permissions.filter(codename__in=["can_view", "can_create", "can_edit"]))
viewers_group.permissions.set(permissions.filter(codename="can_view"))
admins_group.permissions.set(permissions)
