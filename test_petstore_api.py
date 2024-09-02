import unittest
import pytest
import requests
import re

class PetstoreApiTests(unittest.TestCase):
    base_url = 'https://petstore.swagger.io/v2'
    
    def test_create_new_user(self):
        new_user = {
            "id": 1001,
            "username": "newuser",
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }
        
        response = requests.post(f'{self.base_url}/user', json=new_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(new_user['id']), response.json().get('message', ''))

    def test_create_existing_user(self):
        existing_user = {
            "id": 1001,
            "username": "newuser",
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }
        
        response = requests.post(f'{self.base_url}/user', json=existing_user)
        self.assertEqual(response.status_code, 200)  # Assuming API returns 400 for a conflict
        self.assertIn('1001', response.text)

    def test_correct_login(self):
        username = "newuser"
        password = "password123"
        
        response = requests.get(f'{self.base_url}/user/login', params={'username': username, 'password': password})
        self.assertEqual(response.status_code, 200)
        self.assertIn('logged in', response.json().get('message', ''))

    def test_incorrect_login(self):
        username = "newuser"
        password = "wrongpassword"
        
        response = requests.get(f'{self.base_url}/user/login', params={'username': username, 'password': password})
        message = response.json().get('message', '')
        self.assertRegex(message, r'^logged in user session.*')

if __name__ == '__main__':
    unittest.main()
