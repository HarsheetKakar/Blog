from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user(self):
        """Test to create a user"""
        email = 'harsheet@gmail.com'
        password = 'Harsheet1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(email,user.email)
        self.assertTrue(user.check_password(password))
