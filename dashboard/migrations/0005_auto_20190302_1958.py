# Generated by Django 2.1.7 on 2019-03-02 19:58

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190302_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddata',
            name='upload',
            field=models.FileField(default='SIH.csv', upload_to=dashboard.models.user_directory_path),
        ),
    ]
