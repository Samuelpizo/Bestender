# Generated by Django 3.2.7 on 2021-10-13 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0002_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='codigo',
        ),
    ]
