from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import *



urlpatterns = [
    #path('', get_news, name='get_news'),
    #path('post/<int:post_id>/', show_post, name='post'),
    #CRUD
    path('', NewsListView.as_view(), name='news_view'),
    path('news-detail/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news-create/', NewsCreateView.as_view(), name='news_create'),
    path('news-update/<int:pk>/', NewsUpdateView.as_view(), name='news_update'),
    path('news-delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
]

