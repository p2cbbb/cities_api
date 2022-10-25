from rest_framework.test import APITestCase
from api.models import City


class ApiTestClass(APITestCase):
    def setUp(self):
        City.objects.create(city_name="Москва")

    def test_get_city(self):
        url = "http://127.0.0.1:8000/api/city/"
        response = self.client.get(url)
        city = response.json()['cities'][0]['city_name']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(city, "Москва")







