from django.urls import path,include
from ...Views.Auth.Auth import *




urlpatterns=[
path('',AuthView.as_view(),name='AuthView'),
]
