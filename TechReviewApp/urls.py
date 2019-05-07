from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getTypes/', views.getTypes, name='types'),
    path('getProducts/', views.getProducts, name='products'),
    path('productDetail/<int:id>', views.productDetail, name='productdetail'),
]