from django.db import models

from accounts.models import Accounts
from datetime import datetime as dt , timezone
# Create your models here.

class Teams(models.Model):
    team_name = models.CharField(max_length=100, primary_key=True)
    home_ground = models.CharField(max_length=100)
    cups_won = models.CharField(max_length=100, default="")
    image_url = models.ImageField(upload_to ='team_logo', default ="team_logo/code.jpg")
    def __str__(self):
        return self.team_name
    class Meta:
        db_table = "Teams"
class Team_players(models.Model):
    player_first_name = models.CharField(max_length=100)
    player_last_name = models.CharField(max_length=100)
    team_name = models.ForeignKey(Teams, on_delete=models.CASCADE)
    class Meta:
        db_table = "Team_players"
################################################
class Stadium(models.Model):
    city_choice = (
        ('KOLKATA','Kolkata'),
        ('CHENNAI','Chennai'),
        ('DELHI','Delhi'),
        ('MUMBAI','Mumbai'),
        ('KANPUR','Kanpur'),
        ('BANGALORE','Bangalore'),
        ('CUTTACK','Cuttack'),
        ('MOHALI','Mohali'),
        ('VISAKHAPATNAM','Visakhapatnam'),
        ('HYDERABAD','Hyderabad'),
        ('INDORE','Indore'),
        ('NAGPUR','Nagpur'),
        ('PUNE','Pune'),
        ('RAJKOT','Rajkot'),
        ('RANCHI','Ranchi'),
        ('DHARAMSHALA','Dharamshala'),
        ('GUWAHATI','Guwahati'),
        ('THIRUVANANTHAPURAM','Thiruvananthapuram'),
        ('DEHRADUN','Dehradun'),
        ('LUCKNOW','Lucknow'),
    )
    name = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=20, choices=city_choice,null=False)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Stadium"
class Schedule_Match(models.Model):
    Team_A = models.ForeignKey(Teams, on_delete=models.CASCADE)
    Team_B = models.ForeignKey(Teams, on_delete=models.CASCADE,related_name='Team_B')
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    class Meta:
        db_table = "Schedule_Match"


class Seats(models.Model):
    seats = models.CharField(max_length=4)
    match = models.ForeignKey(Schedule_Match, on_delete=models.CASCADE)
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    booked_date = models.DateTimeField(auto_now=True)
    temp_allocated = models.CharField(max_length=5, default="True")
    @staticmethod
    def delete_temp_allocated():
        s = Seats.objects.filter(temp_allocated="True")
        for x in s:
            time = dt.now(timezone.utc) - x.booked_date
            if time.seconds > (10 * 60):
                x.delete()
    class Meta:
        db_table = "Seats"
class Payment(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    seats = models.CharField(max_length=1000,default='')
    price = models.CharField(max_length=10,default='')
    match_id = models.ForeignKey(Schedule_Match, on_delete = models.CASCADE)
    class Meta:
        db_table = "Payment"
class Bank(models.Model):
    card_no = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    name = models.CharField(max_length=200)
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length=2)
    balance = models.FloatField()
    @staticmethod
    def transfer(card_no_to,card_no_from,cvv,name,exp_month,exp_year,amount):
        try:
            from_t = Bank.objects.filter(card_no=card_no_from,cvv=cvv,name=name.upper(),exp_month=exp_month,exp_year=exp_year)
            if len(from_t)==1:
                to_t = Bank.objects.filter(card_no=card_no_to)
                if len(to_t )==1:
                    amount = float(amount)
                    if from_t[0].balance-1000 > amount:
                        from_t[0].balance = from_t[0].balance - amount
                        to_t[0].balance += amount
                        from_t[0].save()
                        to_t[0].save()
                        return('Transaction Success !!!')
                    else:
                        return('Insufficient Balance !')
                else:
                    return('Beneficiary not Found')
            else:
                return('Transfer Failed !!! \n Authentication Failed.')
        except:
            return('Transaction Failed !')
    class Meta:
        db_table = "Bank"





