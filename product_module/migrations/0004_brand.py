# Generated by Django 4.1.7 on 2023-03-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_category_options_productgallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Brand Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Brand Slug')),
                ('is_available', models.BooleanField(default=True, verbose_name='Active/Not')),
            ],
        ),
    ]