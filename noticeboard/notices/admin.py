from django.contrib import admin
from .models import Category, Notice

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_posted')
    list_filter = ('category', 'date_posted')
    search_fields = ('title', 'description')