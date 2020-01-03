from django.contrib import admin

# Register your models here.
from myapp.models import Teams
from myapp.models import Team_players
from myapp.models import Stadium
from myapp.models import Schedule_Match
from myapp.models import Seats
from myapp.models import Payment
from myapp.models import Bank

class TeamsAdmin(admin.ModelAdmin): # Make a class that inherits admin.ModelAdmin
    # Here "EmployeeAdmin" is user defined  
    list_display =  ('team_name','home_ground','cups_won', 'image_url') # list_display is used to list all the collumn to be displayed
    list_filter = ('team_name','home_ground','cups_won', 'image_url') # list_display is used to list all the collumn to be displayed# If any filter is needed then list_filter is to be used.

class Team_playersAdmin(admin.ModelAdmin):
    list_display = ('player_first_name','player_last_name','team_name')
    list_filter =  ('player_first_name','player_last_name','team_name')

class StadiumAdmin(admin.ModelAdmin):
    list_display = ('id','name','city')
    list_filter = ('name','city')

class Schedule_MatchAdmin(admin.ModelAdmin):
    list_display = ('id','Team_A','Team_B','stadium','date','time')
    list_filter = ('id','Team_A','Team_B','stadium','date','time')

class SeatsAdmin(admin.ModelAdmin):
    list_display = ('id','seats','match','user','booked_date','temp_allocated')
    list_filter = ('id','seats','match','user','booked_date','temp_allocated')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','user','date','seats','match_id')
    list_filter = ('id','user','date','seats','match_id')

class BankAdmin(admin.ModelAdmin):
    list_display = ('id','card_no','cvv','name','exp_month','exp_year','balance')
    list_filter = ('id','card_no','cvv','name','exp_month','exp_year','balance')

# Register Here
admin.site.register(Teams, TeamsAdmin)
admin.site.register(Team_players, Team_playersAdmin)
admin.site.register(Stadium, StadiumAdmin)
admin.site.register(Schedule_Match, Schedule_MatchAdmin)
admin.site.register(Seats, SeatsAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Bank, BankAdmin)