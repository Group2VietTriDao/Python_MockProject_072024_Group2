#third-party
from rest_framework import serializers
from rest_framework.permissions import BasePermission

#Local Django
from .models import (
    Contract,
    Employee,
    ServiceRequest,
    Service, 
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