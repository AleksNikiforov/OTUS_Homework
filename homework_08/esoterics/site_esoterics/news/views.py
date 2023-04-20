from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .models import *
from .forms import NewsForm

# удалять новости может только admin сайта
# редактировать и создавать новости может только сотрудник сайта
# выполнять просмотр новости могут только зарегестрированные пользователи



class NewsListView(ListView):
    model = News


class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News


class NewsCreateView(UserPassesTestMixin, CreateView):
    model = News
    form_class = NewsForm
    success_url = '/news'

    def test_func(self):
        return self.request.user.is_staff


class NewsUpdateView(UserPassesTestMixin, UpdateView):
    model = News
    form_class = NewsForm
    success_url = '/news'

    def test_func(self):
        return self.request.user.is_staff


class NewsDeleteView(UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/news'

    def test_func(self):
        return self.request.user.is_superuser