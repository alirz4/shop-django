from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    slug = models.SlugField(max_length=100, verbose_name='Slug')
    price = models.IntegerField(verbose_name='Price')
    is_active = models.BooleanField(default=False, verbose_name='Active/Not')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    slug = models.SlugField(max_length=100, verbose_name='Slug')
    is_active = models.BooleanField(default=False, verbose_name='Active/Not')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
