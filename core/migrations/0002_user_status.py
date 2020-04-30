# Generated by Django 3.0.5 on 2020-04-30 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[('comensal', 1), ('repartidor', 2), ('administrador', 3)], default=1),
        ),
    ]