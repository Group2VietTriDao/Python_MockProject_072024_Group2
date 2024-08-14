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
    userName = models.CharField(max_length=25,null=True,unique=True,)
    password = models.CharField(max_length=30,null=False,)
    email = models.EmailField(max_length=254,null=False,unique=True,)
    status = models.CharField(choices=STATUS_CHOICES,null=True,blank=True,max_length=11,)
    gender = models.CharField(max_length=6,null=False,choices=GENDER_CHOICES,blank=True,)
    avatar = models.ImageField(null=True,blank=True,)
    dateOfBirth = models.DateField(null=True,blank=True,)
    address = models.CharField(max_length=254,null=True,blank=True,)
    phoneNumber = models.CharField(max_length=22,null=True,blank=True,)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(null=True,blank=True,)
    deletedAt = models.DateTimeField(null=True,blank=True,)
    
    class Meta:
        abstract = False

    def __str__(self):
        return self.userName
    
class Employee(User):
    employee_id = models.AutoField(primary_key=True,)
    name = models.CharField (max_length=50,null=False,)

    def __str__(self):
        return self.userName

class Service(models.Model):
    service_id = models.IntegerField(primary_key=True,)
    serviceName = models.IntegerField(null=False,)
    description = models.CharField(max_length=50,blank=True,)
    price = models.DecimalField(decimal_places=2,max_digits=12,)
    createdDate = models.DateTimeField(auto_now_add=True,)
    updatedDate = models.DateTimeField(null=True,blank=True,)

    def __str__(self):
        return self.serviceName

class ServiceRequest(models.Model):
    DONE = "DO"
    INPROGESS = "IN" 
    DELAY = "DE"
    STATUS_CHOICES = {
        DONE: "Done",
        INPROGESS: "In Progress",
        DELAY: "Delay",
    }
    serviceRequest_id = models.AutoField(primary_key=True,)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE,)
    phoneNumber = models.CharField(max_length=22,blank=True,null=False,)
    email = models.EmailField()
    status = models.CharField( max_length=20,choices=STATUS_CHOICES,null=True,blank=True,)
    numberOfGuards = models.IntegerField(default=5,)
    budget = models.DecimalField(max_digits=12,decimal_places=2,)
    address = models.CharField(max_length=254,null=True,blank=True,)
    startDate = models.DateField(null=False,)
    endDate = models.DateField()
    note = models.CharField(max_length=250)
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField()
    deletedAt = models.DateField()

    class Meta:
        abstract = False

    def __str__(self):
        return self.serviceRequest_id


class Contract(ServiceRequest):
    CASH = "CA"
    BANK = "BA"
    PAYMETHOD_CHOICES = {
        CASH: "Cash",
        BANK: "Bank",
    }
    class Rating(models.IntegerChoices):
        VERYGOOD = 5, 'VeryGood'
        GOOD = 4, 'Good'
        NORMAL = 3, 'Normal'
        BAD = 2, 'Bad'
        VERYBAD = 1, 'VeryBad'

    contract_id = models.IntegerField(primary_key=True,)
    price = models.DecimalField(max_digits=12,decimal_places=2,)
    tax = models.DecimalField(max_digits=12,decimal_places=2,)
    paymethod = models.CharField(choices=PAYMETHOD_CHOICES,blank=True,null=False,max_length=4,)
    rating = models.IntegerField(choices=Rating.choices,null=False,blank=True,)
    feedback = models.CharField(max_length=255,)

    def __str__(self):
        return self.contract_id

