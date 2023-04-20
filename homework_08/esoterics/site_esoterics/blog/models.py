from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    mail = models.EmailField(verbose_name='Gmail')
    photo = models.ImageField(upload_to='user_photo/')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')
    info = models.TextField(max_length=500, verbose_name='Краткая информация')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Пользователи'
