from django.urls import path
from . import views







urlpatterns=[

path('<str:page>/',views.index,name='home'),

path('<str:page>/<str:controller>/',views.index,name='index'),

]



