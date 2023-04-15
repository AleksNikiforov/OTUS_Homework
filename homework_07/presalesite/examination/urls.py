from django.urls import path, re_path
import re
from .views import ExaminationListView, delete

urlpatterns = [
    path('', ExaminationListView.as_view(), name='Examination'),
    path('delete/', delete),
]