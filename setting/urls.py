from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.i18n import i18n_patterns
from .Sitemaps import urlpatterns as SitemapUrlpatterns
from django.conf.urls.static import static
from main.Views.Site.Page404 import Page404View;handler404=Page404View.as_view()



urlpatterns=SitemapUrlpatterns

urlpatterns+=[
path('admin/',admin.site.urls),
# path('api/_jwt/',csrf_exempt(include('api._Jwt.Urls.Urls'))),
# path('api/',csrf_exempt(include('api.V1.Urls.Urls'))),
# path('api/v1/',csrf_exempt(include('api.V1.Urls.Urls'))),
path('auth/',include('account.Urls.Urls')),
path('dashboard/',include('dashboard.Urls.Urls')),
path('',include('main.Urls.Urls')),
]

urlpatterns+= i18n_patterns(
prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
