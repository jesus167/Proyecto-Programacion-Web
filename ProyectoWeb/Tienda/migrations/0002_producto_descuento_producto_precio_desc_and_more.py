# Generated by Django 4.0.4 on 2022-06-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descuento',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_desc',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]