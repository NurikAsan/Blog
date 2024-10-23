from django.contrib import admin
from .models import Post, Comment
from modeltranslation.admin import TranslationAdmin


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        return fields + [f"{field}_translation" for field in ('title', 'body')]


@admin.register(Comment)
class CommentAdmin(TranslationAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
