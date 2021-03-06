# Generated by Django 2.1.5 on 2019-12-27 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_match_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule_match',
            name='match',
        ),
        migrations.AddField(
            model_name='schedule_match',
            name='Team_A',
            field=models.CharField(choices=[('CHENNAI SUPER KINGS', 'Chennai Super Kings'), ('DELHI CAPITALS', 'Delhi Capitals'), ('KINGS XI PUNJAB', 'Kings Xi Punjab'), ('KOLKATA KNIGHT RIDERS', 'Kolkata Knight Riders'), ('MUMBAI INDIANS', 'Mumbai Indians'), ('RAJASTHAN ROYALS', 'Rajasthan Royals'), ('ROYAL CHALLENGERS BANGALORE', 'Royal Challengers Bangalore'), ('SUNRISERS HYDERABAD', 'Sunrisers Hyderabad')], default='XYZ', max_length=100),
        ),
        migrations.AddField(
            model_name='schedule_match',
            name='Team_B',
            field=models.CharField(choices=[('CHENNAI SUPER KINGS', 'Chennai Super Kings'), ('DELHI CAPITALS', 'Delhi Capitals'), ('KINGS XI PUNJAB', 'Kings Xi Punjab'), ('KOLKATA KNIGHT RIDERS', 'Kolkata Knight Riders'), ('MUMBAI INDIANS', 'Mumbai Indians'), ('RAJASTHAN ROYALS', 'Rajasthan Royals'), ('ROYAL CHALLENGERS BANGALORE', 'Royal Challengers Bangalore'), ('SUNRISERS HYDERABAD', 'Sunrisers Hyderabad')], default='ABC', max_length=100),
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]
