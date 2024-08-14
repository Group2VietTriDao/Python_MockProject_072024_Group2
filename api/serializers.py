from rest_framework import serializers
from rest_framework.permissions import BasePermission
from .models import User, CreateRole, Employee,ServiceRequest
from .models import Service, Contract

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'role_id', 'employee_id', 'userName', 
                  'password', 'email', 'status', 'avatar', 'gender', 
                  'dateOfBirth', 'address', 'phoneNumber',)        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'   

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('service_id', 'serviceName', 'description', 'price',)

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ('user_id', 'service_id', 'status', 'numberOfGuards',
                  'budget', 'address', 'phoneNumber', 'email',
                  'startDate', 'endDate', 'note',)
        
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('serviceRequest_id', 'status', 'numberOfGuards',
                  'address', 'startDate', 'endDate', 'price', 
                  'tax', 'paymethod',)