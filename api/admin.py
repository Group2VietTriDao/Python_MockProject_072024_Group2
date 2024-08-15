#Django
from django.contrib import admin

#Local Django
from .models import ( 
    CreateRole,
    Contract,
    Employee,
    ServiceRequest,
    Service,
    User,
)


admin.site.register(User)
admin.site.register(CreateRole)
admin.site.register(Employee)
admin.site.register(ServiceRequest)
admin.site.register(Service)
admin.site.register(Contract)
