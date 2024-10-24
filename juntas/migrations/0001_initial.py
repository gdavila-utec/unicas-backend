# Generated by Django 4.2.7 on 2024-10-23 20:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Junta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total_shares', models.IntegerField(default=0)),
                ('share_value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('duration_months', models.IntegerField(default=12)),
                ('fecha_inicio', models.DateField()),
                ('periodo', models.IntegerField(default=1)),
                ('current_month', models.IntegerField(default=1)),
                ('members', models.ManyToManyField(blank=True, related_name='juntas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
