# Generated by Django 3.0.4 on 2020-10-07 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_remove_postmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='writeup',
            field=models.CharField(max_length=550),
        ),
    ]