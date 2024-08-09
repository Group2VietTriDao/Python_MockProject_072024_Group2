from django.urls import path, include
from .views import UserView,UserCreate,UserRetrieve

urlpatterns = [
    path('list', UserView.as_view()),
    path('create', UserCreate.as_view()),
    path('user/<int:user_id>/', UserRetrieve.as_view(), name='user-retrieve'),
]