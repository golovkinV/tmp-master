from django.urls import include, re_path as url

from template.views import echo, filters, extend

urlpatterns = [
    url(r'^echo/$', echo),
    url(r'^filters/$', filters),
    url(r'^extend/$', extend),
]
