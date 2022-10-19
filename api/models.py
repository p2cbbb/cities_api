from django.db import models



class City(models.Model):
    city_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.city_name


class Street(models.Model):
    street_name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.street_name


class Shop(models.Model):
    shop_name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='shop')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='shop')
    house = models.IntegerField()
    opening_time = models.CharField(max_length=10)
    closing_time = models.CharField(max_length=10)
    
    def __str__(self):
        return self.shop_name


