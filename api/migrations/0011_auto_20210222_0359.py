# Generated by Django 3.1.4 on 2021-02-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210221_0520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='address',
            name='postalCode',
        ),
        migrations.RemoveField(
            model_name='address',
            name='staticNumber',
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Rasht', 'Rasht'), ('Shiraz', 'Shiraz'), ('Tehran', 'Tehran'), ('Esfehan', 'Esfehan'), ('Tabriz', 'Tabriz'), ('Mashhad', 'Mashhad')], max_length=500),
        ),
    ]
