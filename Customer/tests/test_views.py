from rest_framework import status
from .test_setup import TestSetUp

class TestCustomerView(TestSetUp):
    
    # def test_customer_invalid_first_name(self):
    #     res = self.client.post(self.create_url, data=self.customer_invalid_first_name, content_type='application/json')
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    # def test_customer_invalid_last_name(self):
    #     res = self.client.post(self.create_url, self.customer_invalid_last_name)
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_customer_invalid_email(self):
    #     res = self.client.post(self.create_url, self.customer_invalid_email)
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_Customer_invalid_date_of_birth(self):
    #     res = self.client.post(self.create_url, self.customer_invalid_date_of_birth)
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_customer_success(self):
    #     res = self.client.post(self.create_url, self.customer)
    #     self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(res.data.get('email'), self.customer.get('email'))
        
    def test_get_customer_success(self):
        response = self.client.get(self.detail_url, self.detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
