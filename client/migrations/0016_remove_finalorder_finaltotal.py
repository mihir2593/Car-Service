# Generated by Django 5.0 on 2024-06-26 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0015_rename_subtotal_finalorder_finaltotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finalorder',
            name='finaltotal',
        ),
    ]
