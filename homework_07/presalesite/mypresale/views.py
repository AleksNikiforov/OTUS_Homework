from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *


menu = [
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Проектно-изыскательские работы", 'url_name': 'design'},
        {'title': "Обследование СПД", 'url_name': 'examination'},
        {'title': "Стендирование", 'url_name': 'poc'},
        {'title': "Монтажные работы", 'url_name': 'install'},
        {'title': "Пуско-наладочные работы", 'url_name': 'comissioning'},
        {'title': "Приемо-сдаточные испытания", 'url_name': 'accept'},
        {'title': "Миграция", 'url_name': 'migration'},
        {'title': "Прочие работы", 'url_name': 'other_jobs'},
        {'title': "Подрядчик", 'url_name': 'subcontractor'},
        {'title': "Другое", 'url_name': 'other'},
        {'title': "Непридвиденные расходы", 'url_name': 'unenxpected'},
        {'title': "Командировочные расходы", 'url_name': 'business_trip'},
        {'title': "Стоимость одного дня", 'url_name': 'rates'},
        ]


def index(request):
    return render(request, 'mypresale/base.html',  {'menu': menu})
  
def about(request):
    return render(request, 'mypresale/about.html')


class DesignListView(ListView):
    model = Design


class PocListView(ListView):
    model = Poc

class InstallListView(ListView):
    model = Install

class ComissioningListView(ListView):
    model = Comissioning

class AcceptListView(ListView):
    model = Accept

class MigrationListView(ListView):
    model = Migration

class Other_jobstionListView(ListView):
    model = Other_jobs

class SubcontractorListView(ListView):
    model = Subcontractor

class OtherListView(ListView):
    model = Other

class UnenxpectedListView(ListView):
    model = Unenxpected

class Business_tripListView(ListView):
    model = Business_trip

class RatesListView(ListView):
    model = Rates


# def design(request): 
#     return HttpResponse('<h1>Проектно-изыскательские работы</h1>')

# def examination(request): 
#     return HttpResponse('<h1>Обследование СПД</h1>')

# def poc(request): 
#     return HttpResponse('<h1>Стендирование</h1>')

# def install(request): 
#     return HttpResponse('<h1>Монтажные работы</h1>')

# def comissioning(request): 
#     return HttpResponse('<h1>Пуско-наладочные работы</h1>')

# def accept(request): 
#     return HttpResponse('<h1>Приемо-сдаточные испытания</h1>')

# def migration(request): 
#     return HttpResponse('<h1>Миграция</h1>')

# def other_jobs(request): 
#     return HttpResponse('<h1>Прочие работы</h1>')

# def subcontractor(request): 
#     return HttpResponse('<h1>Подрядчик</h1>')

# def other(request): 
#     return HttpResponse('<h1>Другое</h1>')

# def unenxpected(request):
#     return HttpResponse('<h1>Непридвиденные расходы</h1>')

# def business_trip(request): 
#     return HttpResponse('<h1>Командировочные расходы</h1>')

# def rates(request): 
#     return HttpResponse('<h1>Стоимость одного дня</h1>')
