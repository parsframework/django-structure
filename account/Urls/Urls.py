from django.urls import path,include
from .Auth import Urls as AuthUrls




urlpatterns=[
path('',include(AuthUrls)),
]
