#Django
from django.urls import reverse
from django.contrib.auth import get_user_model

#Third-party
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

#Create-user
class UserCreateTests(APITestCase):
    def setUp(self):
        #Testing create-admin and permission access
        self.admin_user = User.objects.create_superuser(
            username='admin1',
            email='admin1@example.com',
            password='123456',
        )
        self.client.force_authenticate(user=self.admin_user)
        self.url = reverse('user-create')

    def test_create_user(self):
        data = {
            'username': 'newuser',
            'user_id': '5',
            'role_id': 'Member',
            'status': 'Done',
            'avatar': '',
            'gender': 'Male',
            'date_of_birth': '2000-01-01',
            'email': 'newuser@emxample.com',
            'password': 'newpassword',
            'address': 'None',
            'phone_number': '123456789',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.object.count(), 2) #Testing User-create up to 2 (admin and newuser)
        self.assertEqual(User.objects.get(username='newuser').enamil, 'newuser@example.com')
    
    def test_create_user_unauthenticated(self):
        # Testing logout admin user and permission access
        self.client.force_authenticate(user=None)
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) #Testing Error access

        def test_create_user_without_permission(self):
            # Create non-admin user to test permission access
            non_admin_user = User.objects.create_user(
                username='nonadmin',
                email='nonadmin@example.com',
                password='password',
            )
            self.client.force_authenticate(user=non_admin_user)
            data = {
                'username': 'newuser',
                'email': 'newuser@example.com',
                'password': 'newpassword',
            }
            response = self.client.post(self.url, data, format='jsom')
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) #Testing Error access
