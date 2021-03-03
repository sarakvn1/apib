# Generated by Django 3.1.4 on 2021-02-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_book_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='summary',
        ),
        migrations.AddField(
            model_name='book',
            name='EnSummary',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='FaSummary',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]