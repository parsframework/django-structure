from django.urls import path,include
from ...Views.Dashboard.Dashboard import *



urlpatterns=[
path('',DashboardView.as_view(),name='DashboardView'),
]
