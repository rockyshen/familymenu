# Generated by Django 3.2.4 on 2023-09-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0005_alter_menu_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuimage',
            name='image',
            field=models.ImageField(default=1, upload_to='menu/images'),
            preserve_default=False,
        ),
    ]
