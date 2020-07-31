from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return Post.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.date_updated


class StaticViewSitemap(Sitemap):

    changefreq = 'never'
    priority = 0.5

    def items(self):
        return ['contact']

    def location(self, item):
        return reverse(item)