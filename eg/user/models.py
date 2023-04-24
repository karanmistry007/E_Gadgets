from django.db import models
from django.contrib.auth.models import AbstractUser

# genderChoice =(("Male","male"),("Female","Female"))
# Create your models here.
class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False,null=True)       
    contactnum=models.CharField(max_length=15,null=True)
    # gender=models.CharField(max_length=1,null=True)       
    #age = models.IntegerField(default=0)
    #salary = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'
        
    def __str__(self):
        return self.username 