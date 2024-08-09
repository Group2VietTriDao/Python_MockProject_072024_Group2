from rest_framework import serializers
from rest_framework.permissions import BasePermission
from .models import User
from .models import CreateRole

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','role_id', 'employee_id', 'userName', 
                  'password', 'email', 'status', 'avatar', 'gender', 
                  'dateOfBirth', 'address', 'phoneNumber',)        