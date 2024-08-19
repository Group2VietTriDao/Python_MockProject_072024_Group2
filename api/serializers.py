#third-party
from rest_framework import serializers
from rest_framework.permissions import BasePermission

#Local Django
from .models import (
    Attendance,
    Contract,
    ClassTraining,
    Employee,
    Employee_Training,
    File,
    Notification,
    Mission,
    Profile,
    Report,
    ServiceRequest,
    Service, 
    TrainingCatalog,
    User,
)


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'role_id', 'username', 
                  'password', 'email', 'status', 'avatar', 'gender', 
                  'date_of_birth', 'address', 'phone_number',)        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'   

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('service_id', 'service_name', 'description', 'price',)

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ('user_id', 'service_id', 'status', 'number_of_guards',
                  'budget', 'address', 'phone_number', 'email',
                  'start_date', 'end_date', 'note',)
        
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('service_request_id', 'status', 'number_of_guards',
                  'address', 'start_date', 'end_date', 'price', 
                  'tax', 'paymethod',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_id', 'employee_id', 'link_profile',)

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('report_id', 'user_id', 'contract_id', 'title',
                  'information', 'status', 'file_link_report',)
        
class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ('mission_id', 'contract_id', 'employee_id', 'description',
                  'status', 'task_description', 'address', 'start_date',
                  'end_date', 'salary', 'rating', 'feedback',)

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('attendance_id', 'mission_id', 'status',
                  'checkin_time', 'checkout_time', 'date',)

class TrainingCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCatalog
        fields = ('')

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('notification_id','employee_id', 'user_id', 'title',
                   'msssage', 'created_date',)
    
class ClassTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTraining
        fields = ('class_training_id', 'training_catalog_id', 
                  'name_class_training', 'status', 'start_date',
                  'end_date', 'deleted_at', 'location',)

class EmployeeTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Training
        fields = ('employee_training_id', 'training_catalog_id',
                  'status','description', 'location', 'assess',
                  'start_date', 'end_date',)

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file_id', 'contract_id', 'category_file',
                  'link_file',)
        