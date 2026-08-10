from django.contrib.sitemaps import Sitemap
from db.Site.Site import *



class TestSitemap(Sitemap):

    changefreq='weekly'
    priority=0.8

    def items(self):
        return Site.objects.all()

    def lastmod(self,obj):
        return obj.updated_at

    def location(self,obj):
        return obj.get_absolute_url()
