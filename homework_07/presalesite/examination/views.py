from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *



class CategoryListView(ListView):
    model = Category
    form_class = ExaminationForm


class SubcategoryListView(ListView):
    model = Subcategory
    form_class = ExaminationForm
    
    def get(self, request, *args, **kwargs):
        print(kwargs['pk_cat'])
        print('#'*50)
        self.subcategory_id = kwargs['pk_cat']
        return super().get(request,*args, **kwargs)

    def get_queryset(self):
        return Subcategory.objects.filter(cat_subcategory_id = self.subcategory_id)


class ProductListView(ListView):
    model = Product
    form_class = ExaminationForm

    def get(self, request, *args, **kwargs):
        self.subcategory_id = kwargs['pk_product']
        print(self.subcategory_id)
        print('-'*50)
        return super().get(request,*args, **kwargs)

    def get_queryset(self):
        return Product.objects.filter(subcat_product_id = self.subcategory_id)
    

class SubproductListView(ListView):
    model = Subproduct
    form_class = ExaminationForm

    def get(self, request, *args, **kwargs):
        self.category_id = kwargs['pk_sub_product']
        return super().get(request,*args, **kwargs)

    def get_queryset(self):
        return Subproduct.objects.filter(prod_subproduct_id = self.category_id).order_by('id')
