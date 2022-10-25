from rest_framework.test import APITestCase
from api.models import City, Street


class BaseTest(APITestCase):
    def setUp(self):
        city = City.objects.create(city_name="Москва")
        street = Street.objects.create(street_name="Пушкинская", city=city)


class CityTestClass(BaseTest):
    def test_get_city(self):
        url = "http://127.0.0.1:8000/api/city/"
        response = self.client.get(url)
        cities = response.json()['cities']
        first_city = cities[0]['city_name']
        number_of_cities = len(cities)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(first_city, "Москва")
        self.assertEqual(number_of_cities, 1)

    def test_get_streets_of_city(self):
        city_id = City.objects.get(city_name="Москва").id
        url = f"http://127.0.0.1:8000/api/city/{city_id}/street/"
        response = self.client.get(url)
        streets = response.json()['streets']
        first_street = streets[0]['street_name']
        number_of_streets = len(streets)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(first_street, "Пушкинская")
        self.assertEqual(number_of_streets, 1)




