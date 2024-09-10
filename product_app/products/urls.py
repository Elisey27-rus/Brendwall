from django.urls import path
from .views import product_list, index

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product-list'),
]
