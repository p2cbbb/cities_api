from rest_framework.test import APITestCase
from api.models import City, Street, Shop


class BaseTest(APITestCase):
    def setUp(self):
        self.city = City.objects.create(city_name="Москва")
        self.street = Street.objects.create(street_name="Пушкинская", city=self.city)
        self.shop = Shop.objects.create(shop_name="MagicRainbow", city=self.city, street=self.street, 
                                        house=12, opening_time="10:00:00", closing_time="22:00:00")

class APITestClass(BaseTest):
    def test_get_city(self):
        url = "http://127.0.0.1:8000/api/city/"
        response = self.client.get(url)
        cities = response.json()['cities']
        first_city = cities[0]['city_name']
        number_of_cities = len(cities)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(first_city)
        self.assertEqual(number_of_cities, 1)

    def test_get_streets_of_city(self):
        city_id = City.objects.get(city_name="Москва").id
        url = f"http://127.0.0.1:8000/api/city/{city_id}/street/"
        response = self.client.get(url)
        streets = response.json()['streets']
        first_street = streets[0]['street_name']
        number_of_streets = len(streets)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(first_street)
        self.assertEqual(number_of_streets, 1)

    def test_get_streets_of_unexistent_city(self):
        city_id = 200
        url = f"http://127.0.0.1:8000/api/city/{city_id}/street/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_create_shop(self):
        shop_json = {
            "shop_name": "SoftStore",
            "city": {
                "city_name": "Санкт-Петербург"
            },
            "street": {
                "street_name": "Марата"
            },
            "house": 8,
            "opening_time": "10:00:00",
            "closing_time": "22:00:00"
        }
        url = "http://127.0.0.1:8000/api/shop/"
        response = self.client.post(url, shop_json, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json()['shop_id'])
        self.assertEqual(response.json()['status'], "ok")

    def test_create_shop_with_invalid_data(self):
        shop_json = {
            "shop_name": "SoftStore",
            "city": "Санкт-Петербург",
            "street": "Марата",
            "house": 8,
            "opening_time": "10:00",
            "closing_time": "22:00"
        }
        url = "http://127.0.0.1:8000/api/shop/"
        response = self.client.post(url, shop_json, format='json')
        self.assertEqual(response.status_code, 400)
        
    def test_get_shops_with_only_street_argument(self):
        url = f"http://127.0.0.1:8000/api/shop/?street={self.street.street_name}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['shops'])

    def test_get_shops_with_unexistent_city(self):
        url = f"http://127.0.0.1:8000/api/shop/?city=Лондон"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_get_shops_with_street_and_city_arguments(self):
        url = f"http://127.0.0.1:8000/api/shop/?street={self.street.street_name}&city={self.city.city_name}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['shops'])

    def test_get_shops_with_unexistent_street(self):
        url = f"http://127.0.0.1:8000/api/shop/?street=Советская"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_get_shops_with_street_city_and_open_arguments(self):
        url = f"http://127.0.0.1:8000/api/shop/?street={self.street.street_name}&city={self.city.city_name}&open=1"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['shops'])
        






