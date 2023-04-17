from django.urls import path, re_path
import re
from .views import RatesListView, delete

urlpatterns = [
    path('', RatesListView.as_view(), name='Rates'),
    path('delete/', delete),
]