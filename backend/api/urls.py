from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewsModelView

router = DefaultRouter()

router.register(r'news', NewsModelView, basename="news")

urlpatterns = [
    path('', include(router.urls))
]
