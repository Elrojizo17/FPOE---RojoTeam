# Generated by Django 5.0.3 on 2024-04-06 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_num_botones_mouse_numbotones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouse',
            name='dpi',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='numbotones',
            field=models.IntegerField(),
        ),
    ]