# Generated by Django 2.1.7 on 2019-03-13 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0004_auto_20190313_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='usuario_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]