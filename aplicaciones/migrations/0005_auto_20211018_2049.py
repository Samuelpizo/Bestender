# Generated by Django 3.2.7 on 2021-10-19 01:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0004_producto_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['-fecha']},
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidadA',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidadB',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='producto',
            name='nombreP',
            field=models.CharField(default='...', max_length=30),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipodeTransaccion',
            field=models.CharField(default='', max_length=10),
        ),
    ]
