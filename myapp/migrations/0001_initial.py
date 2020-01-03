# Generated by Django 2.1.5 on 2019-12-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('home_ground', models.CharField(max_length=100)),
                ('cups_won', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Teams',
            },
        ),
    ]