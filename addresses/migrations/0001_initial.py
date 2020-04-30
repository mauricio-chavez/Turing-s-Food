# Generated by Django 3.0.5 on 2020-04-30 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formatted_address', models.CharField(max_length=255, verbose_name='dirección')),
                ('indoor_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='número interior')),
                ('alias', models.CharField(max_length=50, verbose_name='alias')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'dirección',
                'verbose_name_plural': 'direcciones',
            },
        ),
    ]
