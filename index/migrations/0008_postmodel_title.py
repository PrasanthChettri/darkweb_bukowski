# Generated by Django 3.0.4 on 2020-10-07 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_remove_postmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='n', max_length=50),
        ),
    ]