# Generated by Django 5.0.1 on 2024-02-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapi', '0004_alter_content_author_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='doc',
            field=models.FileField(upload_to='pdf/'),
        ),
    ]
