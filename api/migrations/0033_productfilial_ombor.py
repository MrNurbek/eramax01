# Generated by Django 3.1.4 on 2022-04-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20220409_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfilial',
            name='ombor',
            field=models.BooleanField(default=False),
        ),
    ]
