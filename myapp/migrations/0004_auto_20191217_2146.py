# Generated by Django 2.1.5 on 2019-12-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20191217_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='cups_won',
            field=models.CharField(default='', max_length=100),
        ),
    ]
