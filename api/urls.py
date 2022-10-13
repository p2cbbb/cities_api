from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CityView

router = DefaultRouter()
router.register(r'city', CityView, basename="city")

urlpatterns = [
    path('', include(router.urls)),
]
