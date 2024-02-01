from django.urls import reverse
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):
    def setUp(self):
        self.upload_url = reverse('upload')
        self.customer = {
            'id': 1,
            'first_name': 'an',
            'last_name': 'pham',
            'email': 'test123@gmail.com',
            'date_of_birth': '2003-03-15'
        }
        
        self.post = {
            'product_description': 'quan ao',
            'standard_price': 500000,
            'product_finish': 'ok'
        }
        
        self.product_one = {
            'product_description': 'quan ao',
            'product_finish': 'ok',
            'standard_price': 500000,
            'rating': 5,
            'standacommentrd_price': 1000,
            'position': 'ok'
        }
        
        self.product_two = {
            'product_description': 'giay',
            'product_finish': 'ok',
            'standard_price': 300000,
            'rating': 4,
            'standacommentrd_price': 2000,
            'position': 'ok'
        }
 
