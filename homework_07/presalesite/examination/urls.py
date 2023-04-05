from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', ExaminationListView.as_view(), name='Exam'),
    path('examination-create/', ExaminationCreateView.as_view(), name='Exam_create'),
]
