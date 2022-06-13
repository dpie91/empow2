from django.contrib import admin
from .models import Post, Comment

# Register the create model from models.py of how the posts will look


# Define how the admin sees everything
# Do you to add a search field or is that overkill?
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'created', 'author')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
