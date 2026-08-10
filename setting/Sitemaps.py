from django.urls import path
from django.contrib.sitemaps.views import sitemap
from main.Urls.Sitemap.Sitemap import TestSitemap



sitemaps={
'test':TestSitemap,
}

urlpatterns=[
path('sitemap.xml/',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]
