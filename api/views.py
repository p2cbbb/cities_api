from rest_framework import  status
from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response

from .models import City, Street
from .serializers import CitySerializer, StreetSerializer


class CityView(views.APIView):
    def get(self, request):
        streets = City.objects.all()
        serializer = CitySerializer(streets, many=True)
        return Response({"cities": serializer.data}, status=status.HTTP_200_OK)


class StreetsOfCityView(views.APIView):
    def get(self, request, city_id):
        streets = Street.objects.filter(city=city_id).all()
        serializer = StreetSerializer(streets, many=True)
        return Response({"streets": serializer.data}, status=status.HTTP_200_OK)

