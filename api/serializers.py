from rest_framework import serializers

from api.models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('city_name',)
        
        
class StreetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Street
        fields = ('street_name',)
    
    
class ShopSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(max_length=200)
    city = CitySerializer()
    street = StreetSerializer()
    house = serializers.IntegerField()
    opening_time = serializers.CharField(max_length=10)
    closing_time = serializers.CharField(max_length=10)
    
    class Meta:
        model = Shop
        fields = ('shop_name', 'city', 'street', 'house', 'opening_time', 'closing_time')
        
    def create(self, validated_data):
        city_data = validated_data.pop('city')
        city = City.objects.get(city_name=city_data["city_name"])
        street_data = validated_data.pop('street')
        street = Street.objects.get(street_name=street_data["street_name"])
        shop = Shop.objects.create(city=city, street=street, **validated_data)
        return shop
    
