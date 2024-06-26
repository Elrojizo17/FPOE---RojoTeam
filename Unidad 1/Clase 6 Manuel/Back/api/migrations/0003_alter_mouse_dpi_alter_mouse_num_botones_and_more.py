# Generated by Django 5.0.3 on 2024-04-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_mouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouse',
            name='dpi',
            field=models.FloatField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='num_botones',
            field=models.FloatField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='sensor',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
