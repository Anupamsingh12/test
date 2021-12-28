from django.db import models

# Create your models here.

class ApiKey(models.Model):
    
    name=models.CharField(max_length=30,null=True)
    key=models.CharField(max_length=500,null=True)
    

    
    def __str__(self):
        return self.name