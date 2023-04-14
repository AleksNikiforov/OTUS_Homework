from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *



class CategoryListView(ListView):
    model = Category
    form_class = ExaminationForm

    def post(self, request, *args, **kwargs):
        # получаем данные из POST-запроса
        if request.method == 'POST':
            data = request.POST
            #print(dict(data))
            data = {k: v for k, v in data.items() if v is not None and v != ""}
            data.pop("csrfmiddlewaretoken")
            print(data)
            print('='*50)
            # cat = Category(name = 'NTCNN')
            # cat.save()
            print('*'*50)
            return render(request, 'examination/success_add.html')

        

# def my_view(request):
#     if request.method == 'POST':
#         # проверяем, была ли установлена галочка
#         if request.POST.get('html') == 'on':
#             # галочка была установлена
#         else:
#             # галочка не была установлена

#         # обработка полученных данных...

#     return render(request, 'my_template.html')


# def my_view(request):
#     if request.method == 'POST':
#         # получаем значение, введенное пользователем
#         input_value = request.POST.get('float-input')

#         # получаем текст, содержащийся в элементе <label>
#         label_text = 'Трудозатраты, дней:'

#         # обработка полученных данных...

#     return render(request, 'my_template.html')


# def my_view(request):
#     summary_text = request.POST.get('summary_text')

#     # обработка полученных данных...

#     return render(request, 'my_template.html')



class SubcategoryListView(ListView):
    model = Subcategory
    form_class = ExaminationForm
    
    def get(self, request, *args, **kwargs):
        self.subcategory_id = kwargs['pk_cat']
        return super().get(request,*args, **kwargs)

    def get_queryset(self):
        return Subcategory.objects.filter(cat_subcategory_id = self.subcategory_id)


class ProductListView(ListView):
    model = Product
    form_class = ExaminationForm

    def get(self, request, *args, **kwargs):
        self.subcategory_id = kwargs['pk_product']
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
