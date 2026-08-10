from django.urls import path,include
from .Dashboard import Urls as DashboardUrls
from .Admin import Urls as AdminUrls




urlpatterns=[
path('',include(DashboardUrls)),
path('',include(AdminUrls)),
]
