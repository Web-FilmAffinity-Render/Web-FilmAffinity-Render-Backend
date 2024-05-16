from rest_framework.exceptions import ValidationError
from django.test import SimpleTestCase, TestCase
from project.users import serializers

class TestUserSerializer(SimpleTestCase):
     def test_validate_password_usuariosserializer(self):
        self.assertEqual(serializers.UserSerializer().validate_password("Value1"), "Value1")

        with self.assertRaises(ValidationError):
            serializers.UserSerializer().validate_password("value1")

class TestRegistroView(TestCase):
    def test_registroview(self):
        response = self.client.post('/users/signin', {'name': 'qerdassd','email': 'cuerpo@mail.es','password': 'Cuerpo1'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {'name': 'qerdassd','email': 'cuerpo@mail.es'})

class TestLogView(TestCase):

    def test_registroview(self):
        response = self.client.post('/users/signin', {'name': 'qerdassd','email': 'cuerpo@mail.es','password': 'Cuerpo1'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {'name': 'qerdassd','email': 'cuerpo@mail.es'})
    
    def test_login(self):
        response = self.client.post('/users/signin', {'name': 'qerdassd','email': 'cuerpo@mail.es','password': 'Cuerpo1'})
        response = self.client.post('/users/login', {'email': 'cuerpo@mail.es','password': 'Cuerpo1', 'username': 'cuerpo@mail.es'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('session', response.cookies)

    def test_get_info(self):
        response = self.client.post('/users/signin', {'name': 'qerdassd','email': 'cuerpo@mail.es','password': 'Cuerpo1'})
        response = self.client.post('/users/login', {'email': 'cuerpo@mail.es','password': 'Cuerpo1', 'username': 'cuerpo@mail.es'})
        response = self.client.get('/users/me')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'name': 'qerdassd','email': 'cuerpo@mail.es'})

    def test_update_info(self):
        response = self.client.post('/users/signin', {'name': 'qerdassd', 'email': 'cuerpo@mail.es', 'password': 'Cuerpo1'})
        response = self.client.post('/users/login', {'email': 'cuerpo@mail.es','password': 'Cuerpo1', 'username': 'cuerpo@mail.es'})
        response = self.client.put('/users/me', {'name': 'pudassd', 'email': 'cuerpo@maoil.es', 'password': 'Cuerpo1'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/users/me')
        self.assertEqual(response.data, {'name': 'pudassd', 'email': 'cuerpo@maoil.es'})
    
    def test_logout(self):
        response = self.client.post('/users/signin', {'name': 'qerdassd', 'email': 'cuerpo@mail.es', 'password': 'Cuerpo1'})
        response = self.client.post('/users/login', {'email': 'cuerpo@mail.es','password': 'Cuerpo1', 'username': 'cuerpo@mail.es'})
        self.assertIn('session', response.cookies)
        response = self.client.delete('/users/logout')
        self.assertEqual(response.status_code, 204)
        self.assertEqual('',response.cookies['session'].value)  # Session should be cleared
