# Generated by Django 2.1.7 on 2019-03-02 18:24

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddata',
            name='upload',
            field=models.FileField(upload_to=dashboard.models.user_directory_path),
        ),
    ]
