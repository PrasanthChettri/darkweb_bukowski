# Generated by Django 3.0.4 on 2020-10-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20201007_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
