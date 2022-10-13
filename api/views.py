from rest_framework import  status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import City
from .serializers import CitySerializer


class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    http_method_names = ['get']



