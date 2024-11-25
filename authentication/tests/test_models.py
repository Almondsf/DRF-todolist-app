from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_create_user(self):
        user=User.objects.create_user('Oluwafemi', 'oloyedeoluwafemi2019@yahoo.com', 'Password123!@')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'oloyedeoluwafemi2019@yahoo.com')
        
        
    def test_create_super_user(self):
        user=User.objects.create_superuser('Oluwafemi', 'oloyedeoluwafemi2019@yahoo.com', 'Password123!@')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'oloyedeoluwafemi2019@yahoo.com')
        
        
        
    def test_raises_error_when_no_username_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username="",email='oloyedeoluwafemi2019@yahoo.com', password='Password123!@')
        self.assertRaisesMessage(ValueError, 'username must be set')
        
        
    def test_raises_error_when_no_email_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username="Oluwafemi",email='', password='Password123!@')
        self.assertRaisesMessage(ValueError,'email mustt be set')
        