from django.contrib import admin

from blog.models import Post
# Register your models here.

# solr imageadmin
# from sorl.thumbnail.admin import AdminImageMixin
class PostAdmin(admin.ModelAdmin):
    """
    registering Post model to admin
    """
    list_display = ['title', 'author', 'category', 'date_created', 'status', 'views']
    readonly_fields = ['views']
    list_filter = ['status', 'date_created', 'tags', 'category']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_created'
    ordering = ['status', 'date_created']

admin.site.register(Post, PostAdmin)
