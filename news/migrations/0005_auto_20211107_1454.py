# Generated by Django 3.2.8 on 2021-11-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20211104_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='details',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image',
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]