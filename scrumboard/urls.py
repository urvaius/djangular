from django.urls import path
from django.conf.urls import url
from .api import ListApi, CardApi

urlpatterns = [
    path('lists', ListApi.as_view()),
    path('cards', CardApi.as_view())
]
"""
do either way upper seems better lower old way
urlpatterns = [
    url(r'^lists$', ListApi.as_view()),
    url(r'^cards$', CardApi.as_view()),
]
"""