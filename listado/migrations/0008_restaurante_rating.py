# Generated by Django 2.1.7 on 2019-03-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0007_remove_restaurante_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]
