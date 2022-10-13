from rest_framework import serializers

from api.models import City, Street


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('city_name',)
        
        
class StreetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Street
        fields = ('street_name',)
    
