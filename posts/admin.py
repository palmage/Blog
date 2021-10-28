from django.contrib import admin

from .models import Comments, Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'image', 'text', 'pub_date')
    list_display_links = ('id', 'name', 'author', 'text', 'pub_date')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'author', 'parent', 'post', 'image', 'text', 'pub_date'
    )
    list_display_links = ('id', 'author', 'parent', 'post', 'text', 'pub_date')
