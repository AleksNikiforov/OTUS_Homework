from django.urls import path
from .views import *

urlpatterns = [
    path('', get_blog, name='get_blog'),
]
