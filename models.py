from django.db import models



# Create your models here.
class UserDetails(models.Model):
    Name=models.CharField(max_length=20)
    DOB=models.DateField()
    Mob=models.CharField(max_length=10)
    PAN=models.CharField(max_length=10,)
    Address=models.CharField(max_length=20)
    City=models.CharField(max_length=10)
    State=models.CharField(max_length=10)
    Allot=models.IntegerField(default=10000)
    def __str__(self):
        return self.Name

class UserLoan(models.Model):
    Pan=models.CharField(max_length=10)
    Amount=models.IntegerField()  
    Duration=models.IntegerField()
    
    Date=models.DateField()
    def __str__(self):
        return self.Pan

