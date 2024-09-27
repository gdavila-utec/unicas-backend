# Generated by Django 5.1.1 on 2024-09-16 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0007_alter_prestamo_cuota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='cuota',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='monthly_interest',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='remaining_amount',
            field=models.FloatField(null=True),
        ),
    ]
