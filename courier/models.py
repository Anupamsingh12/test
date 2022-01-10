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

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female"),
    ("other", "other"),
    
)
ROLE_TYPES = (
    ("ADMIN", "admin"),
    ("TEACHER", "teacher"),
    ("STUDENT", "student"),
    ("ACCOUNTANT", "accountant"),
    
)
class Profile(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length = 20,
        choices = GENDER_CHOICES,
        default = 'male'
        )
    role = models.CharField(
        max_length = 20,
        choices = ROLE_TYPES,
        default = 'student'
        )
    currentAddress = models.CharField(max_length=200, blank=True)
    permanentAddress = models.CharField(max_length=200, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    contactNumber=models.CharField(max_length=15,blank=True)
    fatherName=models.CharField(max_length=100,blank=True)
    parentsContactNumber=models.CharField(max_length=15,blank=True)
    userImage=models.ImageField(upload_to="profile_pic")
    def __str__(self):
        return "{}'s profile".format(self.user)
