from rest_framework import  status
from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response

from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityView(views.APIView):
    """
    Endpoint: GET/city/
    Получение всех городов из базы
    """
    def get(self, request):
        streets = City.objects.all()
        serializer = CitySerializer(streets, many=True)
        return Response({"cities": serializer.data}, status=status.HTTP_200_OK)


class StreetsOfCityView(views.APIView):
    """
    Endpoint: GET/city/<city_id>/street
    Получение всех улиц города
    """
    def get(self, request, city_id):
        streets = Street.objects.filter(city=city_id).all()
        serializer = StreetSerializer(streets, many=True)
        return Response({"streets": serializer.data}, status=status.HTTP_200_OK)
    
    
class ShopCreationView(views.APIView):
    """
    Endpoint: POST/street
    Создание нового магазина
    """
    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            # если города с названием city нет в базе, то мы создаем новый город
            serializer_city = serializer.validated_data["city"]["city_name"]
            # city_queryset
            if not City.objects.filter(city_name=serializer_city):
                new_city = City.objects.create(city_name=serializer_city)
            # если улицы с названием street нет в базе, то мы создаем новую улицу
            serializer_street = serializer.validated_data["street"]["street_name"]
            if not Street.objects.filter(street_name=serializer_street):
                Street.objects.create(street_name=serializer_street, city=new_city)
            shop = serializer.save()
            return Response({"shop_id": shop.id, "status": "ok"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShopListView(views.APIView):
    def get(self, request):
        pass



