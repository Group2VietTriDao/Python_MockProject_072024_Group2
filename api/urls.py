from django.urls import path, include
from .views import UserView,UserCreate,UserRetrieve
from .views import EmployeeView,EmployeeCreate,EmployeeRetrieve


urlpatterns = [
    path('user/list', UserView.as_view()),
    path('user/create', UserCreate.as_view()),
    path('user/<int:user_id>/', UserRetrieve.as_view(), name='user-retrieve'),
    path('employee/list', EmployeeView.as_view()),
    path('employee/create', EmployeeCreate.as_view()),
    path('employee/<int:employee_id>/', EmployeeRetrieve.as_view(), name='employee-retrieve'),
]