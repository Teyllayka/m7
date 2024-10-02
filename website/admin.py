from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, PDFDocument, Phone, Post, Pages
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    # Add username to fieldsets so admin can set it
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password'),
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    list_display = ['username', 'is_staff']
    ordering = ['pk']

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['phone', 'phone_displayed']
    search_fields = ['phone', 'phone_displayed']


@admin.register(PDFDocument)
class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'view_pdf')
    search_fields = ('title',)

    def view_pdf(self, obj):
        if obj.pdf_file:
            return format_html('<a href="{}" target="_blank">View PDF</a>', obj.pdf_file.url)
        return "No PDF uploaded"

    view_pdf.short_description = 'PDF File'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'photo')  # Include published_at in the list view
    search_fields = ('title', 'content')  # Allow searching by title and content
    list_filter = ('published_at',)  # Filter options by publish date
    ordering = ('-published_at',)  # Order posts by most recent publish date

    # Optional: if you want to show date widget when editing/creating a post in the admin
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'photo', 'published_at'),
        }),
    )


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('page', 'title', 'content')