# Generated by Django 3.2.19 on 2023-06-05 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0005_cotizacion_archivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='archivo',
        ),
    ]
