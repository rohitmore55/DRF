# Generated by Django 5.0.1 on 2024-02-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.BigIntegerField(max_length=10),
        ),
    ]
