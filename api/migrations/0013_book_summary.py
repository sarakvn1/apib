# Generated by Django 3.1.4 on 2021-02-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210222_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
