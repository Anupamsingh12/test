from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser

# Create your models here.
class consignment(models.Model):
    
    name=models.CharField(max_length=30,null=True)
    dest=models.CharField(max_length=50,null=True)
    pincode=models.CharField(max_length=6,null=True)
    email=models.EmailField(max_length=30)
    status=models.CharField(max_length=30,null=True)
    item_weight=models.FloatField()
    contact=models.CharField(max_length=10)

    
    def __str__(self):
        return self.name