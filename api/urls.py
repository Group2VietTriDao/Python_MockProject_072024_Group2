#Django
from django.urls import path, include

#Local Django
from .views import (
    ContractCreate, ContractUpdate, 
    ContractView, ContractRetrieve,
    EmployeeCreate, EmployeeUpdate, 
    EmployeeView, EmployeeRetrieve,
    ServiceCreate, ServiceUpdate, 
    ServiceView, ServiceRetrieve,
    ServiceRequestCreate, ServiceRequestUpdate, 
    ServiceRequestView, ServiceRequestRetrieve,
    UserCreate, UserView, 
    UserUpdate, UserRetrieve,
)


urlpatterns = [
    # User
    path('user/create', UserCreate.as_view()),
    path('user/update', UserUpdate.as_view()),
    path('user/list', UserView.as_view()),
    path('user/<int:user_id>/', UserRetrieve.as_view(), name='user-retrieve'),
    # Employee
    path('employee/create', EmployeeCreate.as_view()),
    path('employee/update', EmployeeUpdate.as_view()),
    path('employee/list', EmployeeView.as_view()),
    path('employee/<int:employee_id>/', EmployeeRetrieve.as_view(), name='employee-retrieve'),
    #Service
    path('service/create', ServiceCreate.as_view()),
    path('service/update', ServiceUpdate.as_view()),
    path('service/list', ServiceView.as_view()),
    path('service/<int:service_id>/', ServiceRetrieve.as_view(), name='service-retrieve'),
    #ServiceRequest
    path('servicereq/create', ServiceRequestCreate.as_view()),
    path('servicereq/update', ServiceRequestUpdate.as_view()),
    path('servicereq/list', ServiceRequestView.as_view()),
    path('servicereq/<int:serviceR_id>/', ServiceRequestRetrieve.as_view(), name='serviceR-retrieve'),
    #Contract
     #ServiceRequest
    path('contract/create', ContractCreate.as_view()),
    path('contract/update', ContractUpdate.as_view()),
    path('contract/list', ContractView.as_view()),
    path('contract/<int:Contract_id>/', ContractRetrieve.as_view(), name='Contract-retrieve'),
]