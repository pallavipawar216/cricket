# Generated by Django 2.1.5 on 2020-01-02 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20191231_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='match_id',
            new_name='match',
        ),
    ]