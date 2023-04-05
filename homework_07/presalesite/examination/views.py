from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import ExaminationForm



class ExaminationListView(ListView):
    model = Examination
    form_class = ExaminationForm


class ExaminationCreateView(CreateView):
    model = Examination
    form_class = ExaminationForm
    success_url = '/examination'