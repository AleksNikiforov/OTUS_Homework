from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    subcategory = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегория'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return self.name
    

class Subproduct(models.Model):
    category = models.ForeignKey(Product, related_name='subproducts', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подпродукт'
        verbose_name_plural = 'Подпродукт'

    def __str__(self):
        return self.name