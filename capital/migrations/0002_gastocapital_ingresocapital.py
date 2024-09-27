# Generated by Django 5.1.1 on 2024-09-17 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GastoCapital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('reserva_legal', 'Reserva Legal'), ('fondo_social', 'Fondo Social')], max_length=255)),
                ('amount', models.FloatField()),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('capital_social', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='capital.capitalsocial')),
            ],
        ),
        migrations.CreateModel(
            name='IngresoCapital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('reserva_legal', 'Reserva Legal'), ('fondo_social', 'Fondo Social')], max_length=255)),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('capital_social', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='capital.capitalsocial')),
            ],
        ),
    ]
