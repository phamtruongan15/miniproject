from rest_framework import status
from .test_setup import TestSetUp

class TestUpLoadView(TestSetUp):
    def test_create_success(self):
        
        with open('Product/tests/dsa.png', '+rb') as file:
            self.post['image'] = file
            print(file)
            res_post = self.client.post(self.upload_url, self.post)
            self.assertEqual(res_post.status_code, status.HTTP_201_CREATED)
           
# class ProductSearchViewTest(TestSetUp):
#     def test_search_product_by_finish(self):
#         response = self.client.get('search',
#                         {'product_finish': 'quan ao'})
#         self.assertEqual(response.status_code, 200)