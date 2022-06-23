from django.urls import include, re_path as url
from django.urls import path
from template.views import *

urlpatterns = [
    path('template/echo/', echo, name='echo'),
    path('template/filters/', filters, name='filters'),
    path('template/extent/', extend, name='extent'),
    path('datasend/', DatasendView.as_view())
]
