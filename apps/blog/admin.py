from django.contrib import admin
from .models import Post, Category, Tag, PostTag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created')
    list_filter = ('status', 'created', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('view_count', 'status', 'created')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PostTag)
