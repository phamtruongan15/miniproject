from rest_framework import status
from .test_setup import TestSetUp
from django.urls import reverse

class TestCustomerView(TestSetUp):
    
    def test_customer_invalid_first_name(self):
        res = self.client.post(self.create_url, data=self.customer_invalid_first_name, content_type='application/json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_customer_invalid_last_name(self):
        res = self.client.post(self.create_url, self.customer_invalid_last_name)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_customer_invalid_email(self):
        res = self.client.post(self.create_url, self.customer_invalid_email)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_customer_invalid_date_of_birth(self):
        res = self.client.post(self.create_url, self.customer_invalid_date_of_birth)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_customer_success(self):
        res = self.client.post(self.create_url, self.customer)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data.get('email'), self.customer.get('email'))
   
        
class TestDeleteView(TestSetUp):
    def test_delete_customer_success(self):
        res = self.client.post(self.create_url, self.customer)  
        url = reverse('customer-delete', kwargs={'pk': res.data.get('id')}) 
        response = self.client.delete(url)
#         # Kiểm tra xem request có thành công không
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
         
    def test_delete_customer_not_found(self):
        # Gọi API endpoint với một ID không tồn tại
        non_existing_customer_id = 9999
        url = reverse('customer-delete', args=[non_existing_customer_id])  
        response = self.client.delete(url)

        # Kiểm tra xem request có trả về 404 Not Found hay không
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestUpdateCustomer(TestSetUp):
    def test_update_customer_success(self):
        # Dữ liệu mới để cập nhật thông tin khách hàng
        new_customer_data = {
            'id':1,
            'first_name': 'do',
            'last_name': 'phan',
            'email': 'phan111@gmail.com',
            'date_of_birth': '1995-02-15'
        }
        # Gọi API endpoint để cập nhật thông tin khách hàng
        res = self.client.post(self.create_url, self.customer)  
        url = reverse('customer-update', kwargs={'pk': res.data.get('id')}) 
        response = self.client.put(url, data=new_customer_data, format='json')
        # Kiểm tra xem request có thành công không
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_customer_not_found(self):
        # Gọi API endpoint để cập nhật thông tin một khách hàng với ID không tồn tại
        non_existing_customer_id = 9999
        url = reverse('customer-update', kwargs={'pk': non_existing_customer_id})
        new_customer_data = {
            'first_name': 'do',
            'last_name': 'phan',
            'email': 'phan111@gmail.com',
            'date_of_birth': '1998-05-20'
        }
        response = self.client.put(url, data=new_customer_data, format='json')

        # Kiểm tra xem request có trả về 404 Not Found hay không
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
 
       
class TestGetCustomer(TestSetUp):
    def test_get_customer_success(self):
        res = self.client.post(self.create_url, self.customer)  
        # Gọi API endpoint để lấy thông tin khách hàng
        url = reverse('customer-detail', kwargs={'pk': res.data.get('id')})
        response = self.client.get(url)
        # Kiểm tra xem request có thành công không
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customer_not_found(self):
        # Gọi API endpoint với một ID không tồn tại
        non_existing_customer_id = 9999
        url = reverse('customer-detail', kwargs={'pk': non_existing_customer_id})
        response = self.client.get(url)
        # Kiểm tra xem request có trả về 404 Not Found hay không
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Kiểm tra xem kết quả có phải là None (không tìm thấy) hay không