# Generated by Django 5.1.1 on 2024-10-11 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_role_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role_type',
            field=models.CharField(choices=[('PRESIDENTE', 'Presidente'), ('SECRETARIO', 'Secretario'), ('TESORERO', 'Tesorero'), ('VOCAL', 'Vocal'), ('SOCIO', 'Socio'), ('NONE', 'None')], default='NONE', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('ADMIN', 'Administrador'), ('FACILITATOR', 'Facilitador'), ('DIRECTOR', 'Directivo'), ('PARTNER', 'Socio')], default='PARTNER', max_length=20),
        ),
    ]
