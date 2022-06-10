from django.urls import include, re_path
from .views import *

urlpatterns = [
    re_path(r'^simple_route/$', simple_route),
    re_path(r'^slug_route/([a-z0-9-_]{1,16})/$', slug_route),
    re_path(r'^sum_route/(-?\d+)/(-?\d+)/$', sum_route),
    re_path(r'^sum_get_method/$', sum_get_method),
    re_path(r'^sum_post_method/$', sum_post_method),
]
