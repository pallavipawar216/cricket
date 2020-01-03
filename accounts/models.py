from django.db import models

# Create your models here.
class Accounts(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.email_id
    class Meta: 
        db_table = "Accounts"
