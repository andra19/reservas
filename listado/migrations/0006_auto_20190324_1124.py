# Generated by Django 2.1.7 on 2019-03-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0005_auto_20190324_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
