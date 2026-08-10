from django.urls import path,include
from .Site import Urls as SiteUrls



urlpatterns=[
path('',include(SiteUrls)),
]
