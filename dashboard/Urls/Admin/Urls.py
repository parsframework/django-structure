from django.urls import path,include
from ...Views.Admin.Admin import *




urlpatterns=[
path('admin/',AdminView.as_view(),name='AdminView'),
]
