# Generated by Django 3.1.4 on 2022-03-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20220318_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chiqimsubcategory',
            name='to_employee',
        ),
        migrations.RemoveField(
            model_name='chiqimsubcategory',
            name='to_supplier',
        ),
        migrations.AddField(
            model_name='chiqimturi',
            name='to_employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chiqimturi',
            name='to_supplier',
            field=models.BooleanField(default=False),
        ),
    ]
