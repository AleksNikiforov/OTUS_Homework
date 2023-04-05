from django import forms
from .models import Examination


class ExaminationForm(forms.ModelForm):

    name = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'placeholder': 'Наименование','class': 'form-control'}))
    days_engineer = forms.CharField(label='Трудозатраты инженер', widget=forms.TextInput(attrs={'placeholder': 'Количество рабочих дней', 'class': 'form-control'}))


    class Meta:
        model = Examination
        #fields = '__all__'
        #fields = ('name', 'foods')
        exclude = ('days_tech_writer', 'days_manager', 'days_architect')