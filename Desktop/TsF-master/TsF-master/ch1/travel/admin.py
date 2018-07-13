from django.contrib import admin
from .models import Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['local', 'name', 'language','visited_country', 'next_country', 'interest', 'content', 'created_at','guide_at','email']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['local_category',]



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)