# Generated by Django 5.0 on 2024-06-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_allorderlist_cartitem_delete_orderlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(default='pending', max_length=255),
        ),
    ]
