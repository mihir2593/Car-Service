# Generated by Django 5.0 on 2024-06-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_confirmorder_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalorder',
            name='subtotal',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]