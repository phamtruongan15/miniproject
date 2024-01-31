
from django.urls import reverse
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):
    def setUp(self):
        self.create_url = reverse('customer-create')
        self.customer = {
            'first_name': 'an',
            'last_name': 'pham',
            'email': 'test123@gmail.com',
            'date_of_birth': '2003-03-15'
        }

        self.customer_invalid_first_name = {
            'first_name': '',
            'last_name': 'Pham',
            'email': 'test123@gmail.com',
            'date_of_birth': '2003/3/15'
        }

        self.customer_invalid_last_name = {
            'first_name': 'An',
            'last_name': '',
            'email': 'test123@gmail.com',
            'date_of_birth': '2003/3/15'
        }

        self.customer_invalid_email = {
            'first_name': 'An',
            'last_name': 'Pham',
            'email': 'test123gmail.com',
            'date_of_birth': '2003/3/15'
        }

        self.customer_invalid_date_of_birth = {
            'first_name': 'An',
            'last_name': 'Pham',
            'email': 'test123gmail.com',
            'date_of_birth': ''
        }
        
    def setUpDetail(self):
        self.detail_url = reverse('customer-detail', kwargs={'customer_pk': self.customer.pk})    
        self.detail = {
            'first_name': 'an',
            'last_name': 'pham',
            'email': 'test123@gmail.com',
            'date_of_birth': '2003-03-15'
        }
        self.detail_not_found = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'date_of_birth': ''
        }
        
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()