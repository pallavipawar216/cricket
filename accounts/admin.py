from django.contrib import admin

# Register your models here.
from accounts.models import Accounts

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email_id','mobile_number','password')
    list_filter = ('id','first_name','email_id','mobile_number','password')

admin.site.register(Accounts,AccountsAdmin)