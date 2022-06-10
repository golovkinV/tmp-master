from django.urls import include, re_path as url
from django.urls import path
from template.views import *

urlpatterns = [
    path('echo/', echo)
    # url(r'^echo/$', echo),
    # url(r'^filters/$', filters),
    # url(r'^extend/$', extend),
]
