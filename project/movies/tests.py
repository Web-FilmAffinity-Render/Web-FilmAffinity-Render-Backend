from django.test import TestCase
from project.users.models import User
from project.movies import serializers, models


class MovieTests(TestCase):
    def test_get_movies(self):
        superuser = User.objects.create_superuser(username='admin', email='admin@email.com', password='easyPassword1')
        _ = self.client.post('/users/login', {'email': 'admin@email.com','password': 'easyPassword1', 'username': 'admin'})
        _ = self.client.post('/movies/create', {'title': 'New Movie', 'year': 2021, 'country': 'Spain', 'director':'Tarantino', 'cast':'aef', 'rate': 6.321, 'genre': 'Action', 'duration': 72, 'plot':'ew'})
        response = self.client.get('/movies')
        self.assertEqual(response.status_code, 301)

    def test_create_movie(self):
        superuser = User.objects.create_superuser(username='admin', email='admin@email.com', password='easyPassword1')
        _ = self.client.post('/users/login', {'email': 'admin@email.com','password': 'easyPassword1', 'username': 'admin'})

        response = self.client.post('/movies/create', {'title': 'New Movie', 'year': 2021, 'country': 'Spain', 'director':'Tarantino', 'cast':'aef', 'rate': 6.321, 'genre': 'Action', 'duration': 72, 'plot':'ew'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get('title'),'New Movie')

class TestUpdateMovie(TestCase):
    def test_update_movie(self):
        superuser = User.objects.create_superuser(username='admin', email='admin@email.com', password='easyPassword1')
        _ = self.client.post('/users/login', {'email': 'admin@email.com','password': 'easyPassword1', 'username': 'admin'})
        _ = self.client.post('/movies/create', {'title': 'New Movie', 'year': 2021, 'country': 'Spain', 'director':'Tarantino', 'cast':'aef', 'rate': 6.321, 'genre': 'Action', 'duration': 72, 'plot':'ew'})
        response = self.client.put('/movies/update/5', {'title': 'Old Movie', 'year': 2021, 'country': 'Spain', 'director':'Tarantino', 'cast':'aef', 'rate': 6.321, 'genre': 'Action', 'duration': 72, 'plot':'ew'},content_type="application/json")
        self.assertEqual(response.status_code, 200)

class TestGetMovie(TestCase):
    def test_get_movie(self):
        superuser = User.objects.create_superuser(username='admin', email='admin@email.com', password='easyPassword1')
        _ = self.client.post('/users/login', {'email': 'admin@email.com','password': 'easyPassword1', 'username': 'admin'})
        _ = self.client.post('/movies/create', {'title': 'New Movie', 'year': 2021, 'country': 'Spain', 'director':'Tarantino', 'cast':'aef', 'rate': 6.321, 'genre': 'Action', 'duration': 72, 'plot':'ew'})
        movie_exists = models.Movie.objects.filter(title='New Movie').exists()
        response = self.client.get('/movies/4')
        self.assertEqual(response.status_code, 200)

class TestDeleteMovie(TestCase):
    def test_delete_movie(self):
        superuser = User.objects.create_superuser(username='admin', email='admin@email.com', password='easyPassword1')
        _ = self.client.post('/users/login', {'email': 'admin@email.com','password': 'easyPassword1', 'username': 'admin'})
        _ = self.client.post('/movies/create', {'title': 'New Movie', 'year': 2021, 'country': 'Spain', 'director':'Tarantino', 'cast':'aef', 'rate': 6.321, 'genre': 'Action', 'duration': 72, 'plot':'ew'})

        response = self.client.delete('/movies/delete/4')
        self.assertEqual(response.status_code, 204)
