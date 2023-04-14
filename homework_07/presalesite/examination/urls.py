from django.urls import path, re_path
import re
from .views import CategoryListView, delete

urlpatterns = [
    path('', CategoryListView.as_view(), name='Category'),
    path('delete/', delete),
]