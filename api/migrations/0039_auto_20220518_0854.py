# Generated by Django 3.1.4 on 2022-05-18 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20220516_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
