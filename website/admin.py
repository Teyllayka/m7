from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Pages, Document
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    # Add username to fieldsets so admin can set it
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'email', 'phone'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'phone'),
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    list_display = ['username', 'is_staff']
    ordering = ['pk']

admin.site.register(CustomUser, CustomUserAdmin)





@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('page', 'content')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('page', 'file', 'uploaded_at')

    def file_link(self, obj):
        return format_html('<a href="{}">{}</a>', obj.file.url, obj.file.name)
    file_link.short_description = 'File'