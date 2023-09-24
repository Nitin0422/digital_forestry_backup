from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.

# User model customized:
class CustomUser(AbstractUser):
    #Disabling unwanted fields.
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(max_length=200, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



class AccountInformation(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    PAN = models.CharField(max_length=200)



class Province(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class LocalLevel(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    def __str__(self):
        return self.name

class Ward(models.Model):
    local_level = models.ForeignKey(LocalLevel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    def __str__(self):
        return self.name
    
class LandInformation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    local_level = models.ForeignKey(LocalLevel, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    kitta_number = models.CharField(max_length=200)
    area = models.FloatField()
    gps_longitude = models.FloatField()
    gps_latitude = models.FloatField()
    is_greater_than_10Ha = models.BooleanField(default=False) 


