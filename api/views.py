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
    Report,
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

class NotificationView(generics.UpdateAPIView):
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

class MissionView(generics.UpdateAPIView):
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

class FileView(generics.UpdateAPIView):
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

class EmployeeTrainingView(generics.UpdateAPIView):
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

class AttendanceView(generics.UpdateAPIView):
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

class ClassTrainingView(generics.UpdateAPIView):
    queryset = ClassTraining.objects.all()
    serializer_class = ClassTrainingSerializer
    permission_classes = [IsAdminUser]

class ClassTrainingRetrieve(generics.RetrieveAPIView):
    queryset = ClassTraining.objects.all()
    serializer_class = ClassTrainingSerializer
    lookup_field = 'classtraining_id'
    permission_classes = [IsAdminUser]

    