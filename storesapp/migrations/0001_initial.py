# Generated by Django 5.0 on 2024-06-18 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('model_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_category', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('c_address', models.CharField(max_length=200)),
                ('c_email', models.EmailField(max_length=254)),
                ('c_phone', models.IntegerField()),
                ('payment_type', models.CharField(max_length=200)),
                ('store_name', models.CharField(max_length=100)),
                ('s_address', models.CharField(max_length=200)),
                ('s_phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='listmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_store_listed', models.DateField()),
                ('o_name', models.CharField(max_length=100)),
                ('s_name', models.CharField(max_length=100)),
                ('s_phonenumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('o_time', models.TimeField()),
                ('c_time', models.TimeField()),
                ('o_phonenumber', models.IntegerField()),
                ('storelicence', models.ImageField(upload_to='storelicence')),
                ('o_documents', models.ImageField(upload_to='documents')),
                ('address', models.CharField(max_length=100)),
                ('s_image', models.ImageField(upload_to='store_image')),
                ('gstno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='storemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('s_phonenumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('o_time', models.TimeField()),
                ('c_time', models.TimeField()),
                ('isavailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='usecategorymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usecategory', models.CharField(max_length=100)),
                ('where_to_use', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product')),
                ('price', models.IntegerField()),
                ('isavailable', models.BooleanField(default=True)),
                ('is_wished', models.BooleanField(default=False)),
                ('Cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storesapp.categorymodel')),
                ('Usecate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storesapp.usecategorymodel')),
            ],
        ),
    ]