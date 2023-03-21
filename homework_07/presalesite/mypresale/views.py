from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    return HttpResponse('<h1>Главная страница</h1>')
  
def about(request): 
    return HttpResponse('<h1>О сайте</h1>')

def design(request): 
    return HttpResponse('<h1>Проектно-изыскательские работы</h1>')

def examination(request): 
    return HttpResponse('<h1>Обследование СПД</h1>')

def poc(request): 
    return HttpResponse('<h1>Стендирование</h1>')

def install(request): 
    return HttpResponse('<h1>Монтажные работы</h1>')

def comissioning(request): 
    return HttpResponse('<h1>Пуско-наладочные работы</h1>')

def accept(request): 
    return HttpResponse('<h1>Приемо-сдаточные испытания</h1>')

def migration(request): 
    return HttpResponse('<h1>Миграция</h1>')

def other_jobs(request): 
    return HttpResponse('<h1>Прочие работы</h1>')

def subcontractor(request): 
    return HttpResponse('<h1>Подрядчик</h1>')

def other(request): 
    return HttpResponse('<h1>Другое</h1>')

def unenxpected(request):
    return HttpResponse('<h1>Непридвиденные расходы</h1>')

def business_trip(request): 
    return HttpResponse('<h1>Командировочные расходы</h1>')

def rates(request): 
    return HttpResponse('<h1>Стоимость одного дня</h1>')
