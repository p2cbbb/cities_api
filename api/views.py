import datetime
from django.shortcuts import get_object_or_404

from rest_framework import  status
from rest_framework import views
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
    
    
class ShopView(views.APIView):
    def post(self, request):
        """
        Endpoint: POST/street
        Создание нового магазина
        """
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
    
    def get(self, request):
        """
        Endpoint: GET/shop/?street=<street_name>&city=<city_name>&open=0/1
        Получение списка магазинов
        """
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        street_name = self.request.query_params.get('street')
        city_name = self.request.query_params.get('city')
        opened = self.request.query_params.get('open')
        shops = Shop.objects.all()
        if street_name:
            street = get_object_or_404(Street, street_name=street_name)
            shops = shops.filter(street=street)
        if city_name:
            city = get_object_or_404(City, city_name=city_name)
            shops = shops.filter(city=city)
        if opened == "1":
            shops = shops.filter(opening_time__lte=current_time, closing_time__gte=current_time)
        elif opened == "0":
            shops = shops.filter(opening_time__gte=current_time, closing_time__lte=current_time)
        
        serializer = ShopSerializer(shops, many=True)
        return Response({"shops": serializer.data}, status=status.HTTP_200_OK)





