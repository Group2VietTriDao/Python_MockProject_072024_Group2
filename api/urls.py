#Django
from django.urls import path, include

#Local Django
from .views import (
    AttendanceCreate, AttendanceUpdate, 
    AttendanceView, AttendanceRetrieve,
    ClassTrainingCreate, ClassTrainingUpdate, 
    ClassTrainingView, ClassTrainingRetrieve,
    ContractCreate, ContractUpdate, 
    ContractView, ContractRetrieve,
    EmployeeCreate, EmployeeUpdate, 
    EmployeeView, EmployeeRetrieve,
    EmployeeTrainingCreate, EmployeeTrainingUpdate, 
    EmployeeTrainingView, EmployeeTrainingRetrieve,
    MissionCreate, MissionUpdate, 
    MissionView, MissionRetrieve,
    FileCreate, FileUpdate, 
    FileView, FileRetrieve,
    ReportCreate, ReportUpdate, 
    ReportView, ReportRetrieve,
    ServiceCreate, ServiceUpdate, 
    ServiceView, ServiceRetrieve,
    ServiceRequestCreate, ServiceRequestUpdate, 
    ServiceRequestView, ServiceRequestRetrieve,
    TrainingCatalogCreate, TrainingCatalogUpdate, 
    TrainingCatalogView, TrainingCatalogRetrieve,
    UserCreate, UserView, 
    UserUpdate, UserRetrieve,
)


urlpatterns = [
    # User
    path('user/create', UserCreate.as_view(), name='user-create'),
    path('user/update', UserUpdate.as_view(), name='user-update'),
    path('user/list', UserView.as_view(), name='user-view'),
    path('user/<int:user_id>/', UserRetrieve.as_view(), name='user-retrieve'),
    # Employee
    path('employee/create', EmployeeCreate.as_view(), name='employee-create'),
    path('employee/update', EmployeeUpdate.as_view(), name='employee-update'),
    path('employee/list', EmployeeView.as_view(), name='employee-view'),
    path('employee/<int:employee_id>/', EmployeeRetrieve.as_view(), name='employee-retrieve'),
    #Service
    path('service/create', ServiceCreate.as_view(), name='service-create'),
    path('service/update', ServiceUpdate.as_view(), name='service-update'),
    path('service/list', ServiceView.as_view(), name='service-view'),
    path('service/<int:service_id>/', ServiceRetrieve.as_view(), name='service-retrieve'),
    #ServiceRequest
    path('servicereq/create', ServiceRequestCreate.as_view(), name='servicereq-create'),
    path('servicereq/update', ServiceRequestUpdate.as_view(), name='servicereq-update'),
    path('servicereq/list', ServiceRequestView.as_view(), name='servicereq-view'),
    path('servicereq/<int:serviceR_id>/', ServiceRequestRetrieve.as_view(), name='serviceR-retrieve'),
    #Contract
    path('contract/create', ContractCreate.as_view(), name='contract-create'),
    path('contract/update', ContractUpdate.as_view(), name='contract-update'),
    path('contract/list', ContractView.as_view(), name='contract-view'),
    path('contract/<int:contract_id>/', ContractRetrieve.as_view(), name='contract-retrieve'),
    #Mission
    path('mission/create', MissionCreate.as_view(), name='mission-create'),
    path('mission/update', MissionUpdate.as_view(), name='mission-update'),
    path('mission/list', MissionView.as_view(), name='mission-view'),
    path('mission/<int:mission_id>/', MissionRetrieve.as_view(), name='mission-retrieve'),
    #File
    path('file/create', FileCreate.as_view(), name='file-create'),
    path('file/update', FileUpdate.as_view(), name='file-update'),
    path('file/list', FileView.as_view(), name='file-view'),
    path('file/<int:file_id>/', FileRetrieve.as_view(), name='file-retrieve'),
    #Report
    path('report/create', ReportCreate.as_view(), name='Report-create'),
    path('report/update', ReportUpdate.as_view(), name='Report-update'),
    path('report/list', ReportView.as_view(), name='Report-view'),
    path('report/<int:report_id>/', ReportRetrieve.as_view(), name='Report-retrieve'),
    #TrainingCatalog
    path('trainingcatalog/create', TrainingCatalogCreate.as_view(), name='trainingcatalog-create'),
    path('trainingcatalog/update', TrainingCatalogUpdate.as_view(), name='trainingcatalog-update'),
    path('trainingcatalog/list', TrainingCatalogView.as_view(), name='trainingcatalog-view'),
    path('trainingcatalog/<int:trainingcatalog_id>/', TrainingCatalogRetrieve.as_view(), name='trainingcatalog-retrieve'),
    #Attendance
    path('attendance/create', AttendanceCreate.as_view(), name='attendance-create'),
    path('attendance/update', AttendanceUpdate.as_view(), name='attendance-update'),
    path('attendance/list', AttendanceView.as_view(), name='attendance-view'),
    path('attendance/<int:attendance_id>/', AttendanceRetrieve.as_view(), name='attendance-retrieve'),
    #ClassTraining
    path('classtraining/create', ClassTrainingCreate.as_view(), name='classtraining-create'),
    path('classtraining/update', ClassTrainingUpdate.as_view(), name='classtraining-update'),
    path('classtraining/list', ClassTrainingView.as_view(), name='classtraining-view'),
    path('classtraining/<int:classtraining_id>/', ClassTrainingRetrieve.as_view(), name='classtraining-retrieve'),
    #EmployeeTraining
    path('employeetraining/create', EmployeeTrainingCreate.as_view(), name='employeetraining-create'),
    path('employeetraining/update', EmployeeTrainingUpdate.as_view(), name='employeetraining-update'),
    path('employeetraining/list', EmployeeTrainingView.as_view(), name='employeetraining-view'),
    path('employeetraining/<int:employee_training_id>/', EmployeeTrainingRetrieve.as_view(), name='employeetraining-retrieve'),
]