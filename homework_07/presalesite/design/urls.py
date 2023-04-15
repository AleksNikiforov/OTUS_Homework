from django.urls import path, re_path
import re
from .views import DesignListView, delete

urlpatterns = [
    path('', DesignListView.as_view(), name='Design'),
    path('delete/', delete),
]