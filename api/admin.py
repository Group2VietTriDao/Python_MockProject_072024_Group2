from django.contrib import admin
from .models import User
from .models import CreateRole
from .models import Employee
from .models import ServiceRequest
from .models import Service
from .models import Contract


# Register your models here.
admin.site.register(User)
admin.site.register(CreateRole)
admin.site.register(Employee)
admin.site.register(ServiceRequest)
admin.site.register(Service)
admin.site.register(Contract)
