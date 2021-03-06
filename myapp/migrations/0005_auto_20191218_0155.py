# Generated by Django 2.1.5 on 2019-12-17 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20191217_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_first_name', models.CharField(max_length=100)),
                ('player_last_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Team_players',
            },
        ),
        migrations.RemoveField(
            model_name='teams',
            name='id',
        ),
        migrations.AlterField(
            model_name='teams',
            name='team_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='team_players',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Teams'),
        ),
    ]
