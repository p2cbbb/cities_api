from django.urls import path

from .views import CityView, StreetsOfCityView

urlpatterns = [
    path('city/', CityView.as_view()),
    path('city/<int:city_id>/street/', StreetsOfCityView.as_view())
]
