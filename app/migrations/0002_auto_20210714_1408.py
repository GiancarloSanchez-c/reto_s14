# Generated by Django 3.2.5 on 2021-07-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='año',
            field=models.IntegerField(null=True, verbose_name='Año del Modelo'),
        ),
        migrations.AddField(
            model_name='auto',
            name='precio',
            field=models.IntegerField(null=True, verbose_name='Precio'),
        ),
    ]
