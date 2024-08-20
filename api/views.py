#Django
from django.shortcuts import render

#Third-party
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

#Local Django
from .models import( 
    Attendance,
    ClassTraining,
    Contract,
    User,
    Employee,
    Employee_Training,
    File,
    Mission,
    Notification, 
    Report,
    TrainingCatalog,
    Profile,
    Service, 
    ServiceRequest, 
)
from .serializers import (
    AttendanceSerializer,
    ClassTrainingSerializer,
    ContractSerializer,
    UserSerializer,
    EmployeeSerializer,
    EmployeeTrainingSerializer,
    FileSerializer,
    MissionSerializer,
    NotificationSerializer,
    ReportSerializer,
    TrainingCatalogSerializer,
    Profile,
    ServiceRequestSerializer, 
    ServiceSerializer, 
 )


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'
    permission_classes = [IsAdminUser]

class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]

class EmployeeView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]

class EmployeeUpdate(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]

class EmployeeRetrieve(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employee_id'
    permission_classes = [IsAdminUser]

class ServiceCreate(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]

class ServiceUpdate(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]

class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]

class ServiceRetrieve(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'service_id'
    permission_classes = [IsAdminUser]

class ServiceRequestCreate(generics.CreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAdminUser]

class ServiceRequestView(generics.ListAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAdminUser]

class ServiceRequestUpdate(generics.UpdateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAdminUser]

class ServiceRequestRetrieve(generics.RetrieveAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer   
    lookup_field = 'service_request_id'
    permission_classes = [IsAdminUser]

class ContractCreate(generics.ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAdminUser]

class ContractView(generics.ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAdminUser]

class ContractUpdate(generics.UpdateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAdminUser]

class ContractRetrieve(generics.RetrieveAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = 'contract_id'
    permission_classes = [IsAdminUser]

class NotificationCreate(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminUser]

class NotificationView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminUser]

class NotificationRetrieve(generics.RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field = 'Notification_id'
    permission_classes = [IsAdminUser]

class MissionCreate(generics.CreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [IsAdminUser]

class MissionUpdate(generics.UpdateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [IsAdminUser]

class MissionView(generics.ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [IsAdminUser]

class MissionRetrieve(generics.RetrieveAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    lookup_field = 'mission_id'
    permission_classes = [IsAdminUser]

class FileCreate(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAdminUser]

class FileView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAdminUser]

class FileUpdate(generics.UpdateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAdminUser]    

class FileRetrieve(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    lookup_field = 'File_id'
    permission_classes = [IsAdminUser]

class EmployeeTrainingCreate(generics.CreateAPIView):
    queryset = Employee_Training.objects.all()
    serializer_class = EmployeeTrainingSerializer
    permission_classes = [IsAdminUser]

class EmployeeTrainingUpdate(generics.UpdateAPIView):
    queryset = Employee_Training.objects.all()
    serializer_class = EmployeeTrainingSerializer
    permission_classes = [IsAdminUser]

class EmployeeTrainingView(generics.ListAPIView):
    queryset = Employee_Training.objects.all()
    serializer_class = EmployeeTrainingSerializer
    permission_classes = [IsAdminUser]

class EmployeeTrainingRetrieve(generics.RetrieveAPIView):
    queryset = Employee_Training.objects.all()
    serializer_class = EmployeeTrainingSerializer
    lookup_field = 'employee_training_id'
    permission_classes = [IsAdminUser]

class AttendanceCreate(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminUser]

class AttendanceUpdate(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminUser]

class AttendanceView(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminUser]

class AttendanceRetrieve(generics.RetrieveAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    lookup_field = 'attendance_id'
    permission_classes = [IsAdminUser]

class ClassTrainingCreate(generics.CreateAPIView):
    queryset = ClassTraining.objects.all()
    serializer_class = ClassTrainingSerializer
    permission_classes = [IsAdminUser]

class ClassTrainingUpdate(generics.UpdateAPIView):
    queryset = ClassTraining.objects.all()
    serializer_class = ClassTrainingSerializer
    permission_classes = [IsAdminUser]

class ClassTrainingView(generics.ListAPIView):
    queryset = ClassTraining.objects.all()
    serializer_class = ClassTrainingSerializer
    permission_classes = [IsAdminUser]

class ClassTrainingRetrieve(generics.RetrieveAPIView):
    queryset = ClassTraining.objects.all()
    serializer_class = ClassTrainingSerializer
    lookup_field = 'classtraining_id'
    permission_classes = [IsAdminUser]

class ReportCreate(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]

class ReportUpdate(generics.UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]

class ReportView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]

class ReportRetrieve(generics.RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'report_id'
    permission_classes = [IsAdminUser]

class TrainingCatalogCreate(generics.CreateAPIView):
    queryset = TrainingCatalog.objects.all()
    serializer_class = TrainingCatalogSerializer
    permission_classes = [IsAdminUser]

class TrainingCatalogUpdate(generics.UpdateAPIView):
    queryset = TrainingCatalog.objects.all()
    serializer_class = TrainingCatalogSerializer
    permission_classes = [IsAdminUser]

class TrainingCatalogView(generics.ListAPIView):
    queryset = TrainingCatalog.objects.all()
    serializer_class = TrainingCatalogSerializer
    permission_classes = [IsAdminUser]

class TrainingCatalogRetrieve(generics.RetrieveAPIView):
    queryset = TrainingCatalog.objects.all()
    serializer_class = TrainingCatalogSerializer
    lookup_field = 'training_catalog_id'
    permission_classes = [IsAdminUser]

