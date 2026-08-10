from django.urls import path,include
from ...Views.Site.Site import *



urlpatterns=[
path('',HomeView.as_view(),name='HomeView'),
path('404/',Page404View.as_view(),name='Page404View'),
]
