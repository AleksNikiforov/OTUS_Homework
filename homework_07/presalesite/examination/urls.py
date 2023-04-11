from django.urls import path, re_path
import re
from .views import CategoryListView, SubcategoryListView, ProductListView, SubproductListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='Category'),
    path('sub-category/<int:pk_cat>/', SubcategoryListView.as_view(), name='Sub-category'),
    path('sub-category/<int:pk_cat>/product/<int:pk_product>/', ProductListView.as_view(), name='Product'),
    path('sub-category/<int:pk_cat>/product/<int:pk_product>/sub-product/<int:pk_sub_product>/', SubproductListView.as_view(), name='Sub-product'),
]