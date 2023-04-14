from django.urls import path, re_path
import re
from .views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='Category'),
]