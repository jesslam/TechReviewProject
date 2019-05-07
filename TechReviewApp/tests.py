from django.test import TestCase
from django.urls import reverse
from .models import TechType, Product, Review
from django.contrib.auth.models import User

# Create your tests here.
class TechTypeTest(TestCase): 
    def test_string(self):
        type=TechType(techtypename='laptop')
        self.assertEqual(str(type), type.techtypename)

    def test_table(self):
        self.assertEqual(str(TechType._meta.db_table), 'techtype')

class ProductTest(TestCase):
    def setUp(self):
        self.type=TechType(techtypename='tablet')
        self.prod=Product(productname='Ipad', techtype=self.type, productprice=800)
        
    def test_string(self):
        self.assertEqual(str(self.prod), self.prod.productname)

    def test_type(self):
        self.assertEqual(str(self.prod.techtype), 'tablet')

    def test_discount(self):
        self.assertEqual(self.prod.memberDiscount(), 40.00)

# Tests for Views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetProductsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.type=TechType.objects.create(techtypename='laptop')
        self.prod=Product.objects.create(productname='product1', techtype=self.type, 
        user=self.u, productprice=500.00, productentrydate='2019-04-02', 
        productdescription='some kind of laptop')

    def test_product_detail_success(self):
        response=self.client.get(reverse('productdetail', args=(self.prod.id,)))
        self.assertEqual(response.status_code, 200)