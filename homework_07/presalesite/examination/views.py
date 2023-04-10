from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *



class CategoryListView(ListView):
    model = Category
    form_class = ExaminationForm

    def get_queryset(self):
        return Category.objects.all()  


class SubcategoryListView(ListView):
    model = Subcategory
    form_class = ExaminationForm

    def get_queryset(self):
        #category_id = self.kwargs['category_id']
        return Subcategory.objects.filter(subcategory_id = 1) 

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category_id'] = self.kwargs['category_id']
    #     return context



class ProductListView(ListView):
    model = Product
    form_class = ExaminationForm

    def get_queryset(self):
        return Product.objects.filter(category_id = 2) 
    

class SubproductListView(ListView):
    model = Subproduct
    form_class = ExaminationForm

    def get_queryset(self):
        return Subproduct.objects.filter(category_id = 9)  
    
# class ExaminationCreateView(CreateView):
#     #model = Examination
#     form_class = ExaminationForm
#     success_url = '/examination'