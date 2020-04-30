# Generated by Django 3.0.5 on 2020-04-30 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addresses', '0002_auto_20200430_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('latitude', models.FloatField(verbose_name='latitud')),
                ('longitude', models.FloatField(verbose_name='longitud')),
                ('indoor_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='número interior')),
                ('alias', models.CharField(max_length=50, verbose_name='alias')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'dirección de usuario',
                'verbose_name_plural': 'direcciones de usuarios',
            },
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]