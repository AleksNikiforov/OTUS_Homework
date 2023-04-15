from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import *
from .forms import *



class ExaminationListView(ListView):
    model = Examination
    form_class = ExaminationForm
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST
            data = {k: v for k, v in data.items() if v is not None and v != ""}            # удаляем лишние поля из словаря
            data.pop("csrfmiddlewaretoken")                                                # удаляем лишние поля из словаря
            data = {key: value for key, value in data.items() if key != value}             # удаляем лишние поля из словаря
            checked = data['checked_items'].split(',')                                     # разделяем checked_items и создаем список из его значений
            data.pop("checked_items")                                                      # удаляем checked_items из словаря
            for item in checked:                                                           # значениям на против которые стоят галочки ставим значение клоичества дней Null
                data[item] = None
            for n in data.items():                                                         # добавляем записи в БД
                name = n[0]
                days = n[1]
                if days:
                    cat = Examination(name = name, days = days)
                    cat.save()
                else:
                    cat = Examination(name = name)
                    cat.save()   
            return render(request, 'examination/success_add.html')

        

def delete(request):
    Examination.objects.all().delete()
    return redirect(reverse_lazy('Examination'))


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



# class SubcategoryListView(ListView):
#     model = Subcategory
#     form_class = ExaminationForm
    
#     def get(self, request, *args, **kwargs):
#         self.subcategory_id = kwargs['pk_cat']
#         return super().get(request,*args, **kwargs)

#     def get_queryset(self):
#         return Subcategory.objects.filter(cat_subcategory_id = self.subcategory_id)


# class ProductListView(ListView):
#     model = Product
#     form_class = ExaminationForm

#     def get(self, request, *args, **kwargs):
#         self.subcategory_id = kwargs['pk_product']
#         return super().get(request,*args, **kwargs)

#     def get_queryset(self):
#         return Product.objects.filter(subcat_product_id = self.subcategory_id)
    

# class SubproductListView(ListView):
#     model = Subproduct
#     form_class = ExaminationForm

#     def get(self, request, *args, **kwargs):
#         self.category_id = kwargs['pk_sub_product']
#         return super().get(request,*args, **kwargs)

#     def get_queryset(self):
#         return Subproduct.objects.filter(prod_subproduct_id = self.category_id).order_by('id')
