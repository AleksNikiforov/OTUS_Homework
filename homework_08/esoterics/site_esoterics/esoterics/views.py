from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse



# menu = [{'title': "Блог", 'url_name': 'blog'},
#         {'title': "Новости", 'url_name': 'news'},
#         {'title': "Цены", 'url_name': 'price'},
#         {'title': "Контакты", 'url_name': 'contacts'}]

def index(request):
    return render(request, 'esoterics/index.html')

def price(request):
    return HttpResponse("Цены")

def contacts(request):
    return HttpResponse("Контакты")