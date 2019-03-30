# Generated by Django 2.1.7 on 2019-03-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='restaurant_pics')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=200)),
                ('horarios', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('fumar', models.CharField(max_length=100)),
                ('WIFI', models.CharField(max_length=100)),
                ('estacionamiento', models.CharField(max_length=100)),
                ('tarjetas', models.CharField(max_length=100)),
                ('tipoComida', models.CharField(max_length=100)),
                ('comentarios', models.TextField(max_length=500)),
            ],
        ),
    ]