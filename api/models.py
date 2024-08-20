#Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class CreateRole(models.Model):
    class RoleName(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        STAFF = "STAFF", _("Staff")
        MEMBER = "MEMBER", _("Member")
    role_id = models.IntegerField(primary_key=True,unique=True)
    role_name = models.CharField(max_length=6, choices=RoleName,default=RoleName.MEMBER,)
    description = models.TextField()

    def __str__(self):
        return self.role_name

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
    username = models.CharField(max_length=25,null=True,unique=True,)
    password = models.CharField(max_length=30,null=False,)
    email = models.EmailField(max_length=254,null=False,unique=True,)
    status = models.CharField(choices=STATUS_CHOICES,null=True,blank=True,max_length=11,)
    gender = models.CharField(max_length=6,null=False,choices=GENDER_CHOICES,blank=True,)
    avatar = models.ImageField(null=True,blank=True,)
    date_of_birth = models.DateField(null=True,blank=True,)
    address = models.CharField(max_length=254,null=True,blank=True,)
    phone_number = models.CharField(max_length=22,null=True,blank=True,)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True,blank=True,)
    deleted_at = models.DateTimeField(null=True,blank=True,)
    
    class Meta:
        abstract = False

    def __str__(self):
        return self.username
    
class Employee(User):
    employee_id = models.AutoField(primary_key=True,)
    name = models.CharField (max_length=50,null=False,)

    def __str__(self):
        return self.username

class Notification(User):
    notification_id = models.AutoField(primary_key=True,)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE,)
    titile = models.CharField(max_length=100,)
    message = models.CharField(max_length=255,)

class Service(models.Model):
    service_id = models.IntegerField(primary_key=True,)
    service_name = models.IntegerField(null=False,)
    description = models.CharField(max_length=50,blank=True,)
    price = models.DecimalField(decimal_places=2,max_digits=12,)
    created_date = models.DateTimeField(auto_now_add=True,)
    updated_date = models.DateTimeField(null=True,blank=True,)

    def __str__(self):
        return self.service_name

class ServiceRequest(models.Model):
    DONE = "DO"
    INPROGESS = "IN" 
    DELAY = "DE"
    STATUS_CHOICES = {
        DONE: "Done",
        INPROGESS: "In Progress",
        DELAY: "Delay",
    }
    service_request_id = models.AutoField(primary_key=True,)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE,)
    phone_number = models.CharField(max_length=22,blank=True,null=False,)
    email = models.EmailField()
    status = models.CharField( max_length=20,choices=STATUS_CHOICES,null=True,blank=True,)
    number_of_guards = models.IntegerField(default=5,)
    budget = models.DecimalField(max_digits=12,decimal_places=2,)
    address = models.CharField(max_length=254,null=True,blank=True,)
    start_date = models.DateField(null=False,)
    end_date = models.DateField()
    note = models.CharField(max_length=250)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField()
    deleted_at = models.DateField()
    
    class Meta:
        abstract = False

    def __str__(self):
        return self.service_request_id

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

    class Meta:
        abstract = False

    def __str__(self):
        return self.contract_id

class File(models.Model):
    file_id = models.AutoField(primary_key=True,)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE,)
    category_file = models.CharField(max_length=255,)
    linkFile = models.CharField(max_length=255,)

class Profile(Employee):
    profile_id = models.AutoField(primary_key=True,)
    title = models.CharField(max_length=100,blank=True,)
    message = models.CharField(max_length=255,blank=True,)
    link_profile = models.CharField(max_length=255,)

    def __str__(self):
        return self.profile_id

class Report(models.Model):
    report_id = models.AutoField(primary_key=True,)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100,blank=True,)
    informaition = models.CharField(max_length=255,blank=True,)
    status = models.CharField(max_length=20,blank=True,)
    file_link_report = models.CharField(max_length=100,blank=True,)
    created_date = models.DateField(auto_now_add=True,)

class Mission(Contract):
    mission_id = models.AutoField(primary_key=True,)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE,)
    description = models.CharField(max_length=255,blank=False,)
    task_description = models.CharField(max_length=255,blank=False,)
    salary = models.DecimalField(max_digits=10,decimal_places=2,)
    
    def __str__(self):
        return self.mission_id
    
class Attendance(Mission):
    attendance_id = models.AutoField(primary_key=True,)
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()
    date = models.DateField()

class TrainingCatalog(models.Model):
    training_catalog_id = models.AutoField(primary_key=True,)
    training_catalog_name = models.CharField(max_length=255,)
    description = models.CharField(max_length=255,)
    duration = models.CharField(max_length=255,)
    certificate = models.BooleanField(default=True,)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField()
    
class ClassTraining(models.Model):
    class_training_id = models.AutoField(primary_key=True,)
    training_catalog_id = models.ForeignKey(TrainingCatalog, on_delete=models.CASCADE,) 
    name_class_training = models.CharField(max_length=255,)
    status = models.CharField(max_length=20,)
    descritption = models.CharField(max_length=255,)
    location = models.CharField(max_length=255,)
    start_date = models.DateField()
    end_date = models.DateField()
    deleted_at = models.DateField()

class Employee_Training(Employee):
    employee_training_id = models.AutoField(primary_key=True,)
    class_training_id = models.ForeignKey(ClassTraining, on_delete=models.CASCADE,)
    assess = models.CharField(max_length=255,)