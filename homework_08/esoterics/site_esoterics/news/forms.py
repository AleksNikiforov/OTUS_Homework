from django import forms
from .models import News


class NewsForm(forms.ModelForm):

    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'placeholder': 'Краткое описание новости','class': 'form-control'}))
    content = forms.CharField(label='Подробное описание', widget=forms.Textarea(attrs={'placeholder': 'Подробное описание новости', 'class': 'form-control'}))

    class Meta:
        model = News
        fields = '__all__'