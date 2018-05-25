from .api import ListViewSet, CardViewSet
from rest_framework.routers import DefaultRouter

ROUTER = DefaultRouter()
ROUTER.register(r'lists', ListViewSet)
ROUTER.register(r'cards', CardViewSet)

urlpatterns = ROUTER.urls

"""
urlpatterns = [
    path('lists', ListApi.as_view()),
    path('cards', CardApi.as_view()),
    path('home', TemplateView.as_view(template_name="scrumboard/home.html")),
]
"""
"""
do either way upper seems better lower old way
urlpatterns = [
    url(r'^lists$', ListApi.as_view()),
    url(r'^cards$', CardApi.as_view()),
]
"""
