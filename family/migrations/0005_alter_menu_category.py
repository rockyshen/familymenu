# Generated by Django 3.2.4 on 2023-09-27 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0004_auto_20230927_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='family.category'),
        ),
    ]