from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CreateRole(models.Model):
    class RoleName(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        STAFF = "STAFF", _("Staff")
        MEMBER = "MEMBER", _("Member")
    role_id = models.IntegerField(primary_key=True,unique=True)
    roleName = models.CharField(max_length=6, choices=RoleName,default=RoleName.MEMBER,)
    description = models.TextField()
    def __str__(self):
        return self.roleName

class User(models.Model):
    MALE = "MA"
    FEMALE = "FE"
    DONE = "DO"
    INPROGESS = "IN" 
    DELAY = "DE"
    GENDER_CHOICES = {
        MALE: "Male",
        FEMALE: "Female",
    }
    STATUS_CHOICES = {
        DONE: "Done",
        INPROGESS: "In Progress",
        DELAY: "Delay",
    }
    role_id = models.ForeignKey(CreateRole, on_delete=models.CASCADE)
    user_id = models.IntegerField(null=False,primary_key=True,unique=True,)
    employee_id = models.IntegerField(null=True,unique=True,blank=True,)
    userName = models.CharField(max_length=25,null=True,unique=True,)
    password = models.CharField(max_length=30,null=False,)
    email = models.EmailField(max_length=254,null=False,unique=True,)
    status = models.CharField( max_length=20,choices=STATUS_CHOICES,null=True,blank=True,)
    gender = models.CharField(max_length=6,null=False,choices=GENDER_CHOICES,blank=True,)
    avatar = models.ImageField(null=True,blank=True,)
    dateOfBirth = models.DateField(null=True,blank=True,)
    address = models.CharField(max_length=254,null=True,blank=True,)
    phoneNumber = models.CharField(max_length=22,null=True,blank=True,)

    def __str__(self):
        return self.userName
    
    