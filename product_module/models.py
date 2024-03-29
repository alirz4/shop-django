from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', db_index=True)
    slug = models.SlugField(max_length=100, verbose_name='Slug', unique=True, db_index=True)
    image = models.ImageField(upload_to='products', verbose_name='Image', null=True, blank=True)
    price = models.IntegerField(verbose_name='Price', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='Active/Not')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category', blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='product', verbose_name='Brand',
                              null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', db_index=True)
    slug = models.SlugField(max_length=100, verbose_name='Slug', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='Active/Not')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class ProductGallery(models.Model):
    image = models.ImageField(upload_to='prod_gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')

    def __str__(self):
        return self.product.name


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Brand Name')
    slug = models.SlugField(max_length=100, verbose_name='Brand Slug')
    is_available = models.BooleanField(default=True, verbose_name='Active/Not')

    def str(self):
        return self.name
