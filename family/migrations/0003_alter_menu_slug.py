# Generated by Django 3.2.4 on 2023-09-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_auto_20230927_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]