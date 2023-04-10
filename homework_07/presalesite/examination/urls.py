from django.urls import path, re_path
from .views import CategoryListView, SubcategoryListView, ProductListView, SubproductListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='Exam'),
    path('sub-category/', SubcategoryListView.as_view(), name='Sub-category'),
    path('sub-category/product/', ProductListView.as_view(), name='Product'),
    path('sub-category/product/sub-product/', SubproductListView.as_view(), name='Sub-product'),
]
