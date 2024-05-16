from django.test import TestCase
from project.users.models import User

class ReviewTests(TestCase):
    def test_createreview(self):
        superuser = User.objects.create_superuser(username='admin@email.es', email='admin@email.com', password='easyPassword1')
        _ = self.client.post('/users/login', {'email': 'admin@email.com','password': 'easyPassword1', 'username': 'admin@email.es'})
        _ = self.client.post('/movies/create', {'title': 'New Movie', 'year': 2021, 'country': 'Spain', 'director':'Tarantino', 'cast':'aef', 'rate': 6.321, 'genre': 'Action', 'duration': 72, 'plot':'ew'})
        response = self.client.post('/reviews/new',{'movie_title':'New Movie', 'user_username':'admin@email.com','review_text':'sff','review_rate':5.4})
        self.assertEqual(response.status_code, 201)

    def test_createreview_unlogged(self):
        superuser = User.objects.create_superuser(username='admin@email.es', email='admin@email.com', password='easyPassword1')
        _ = self.client.post('/users/login', {'email': 'admin@email.com','password': 'easyPassword1', 'username': 'admin@email.es'})
        _ = self.client.post('/movies/create', {'title': 'New Movie', 'year': 2021, 'country': 'Spain', 'director':'Tarantino', 'cast':'aef', 'rate': 6.321, 'genre': 'Action', 'duration': 72, 'plot':'ew'})
        _ = self.client.delete('/users/logout')
        response = self.client.post('/reviews/new',{'movie_title':'New Movie', 'user_username':'admin@email.com','review_text':'sff','review_rate':5.4})
        self.assertEqual(response.status_code, 401)

    def test_get_reviews_loged(self):
        superuser = User.objects.create_superuser(username='admin@email.es', email='admin@email.com', password='easyPassword1')
        _ = self.client.post('/users/login', {'email': 'admin@email.com','password': 'easyPassword1', 'username': 'admin@email.es'})
        _ = self.client.post('/movies/create', {'title': 'NewMovie', 'year': 2021, 'country': 'Spain', 'director':'Tarantino', 'cast':'aef', 'rate': 6.321, 'genre': 'Action', 'duration': 72, 'plot':'ew'})
        _ = self.client.post('/reviews/new',{'movie_title':'NewMovie', 'user_username':'admin@email.com','review_text':'sff','review_rate':5.4})
        response = self.client.get('/reviews/?movie_title=NewMovie')
        self.assertEqual(response.status_code, 200)

    def test_get_revires_unlogged(self):
        superuser = User.objects.create_superuser(username='admin@email.es', email='admin@email.com', password='easyPassword1')
        _ = self.client.post('/users/login', {'email': 'admin@email.com','password': 'easyPassword1', 'username': 'admin@email.es'})
        _ = self.client.post('/movies/create', {'title': 'NewMovie', 'year': 2021, 'country': 'Spain', 'director':'Tarantino', 'cast':'aef', 'rate': 6.321, 'genre': 'Action', 'duration': 72, 'plot':'ew'})
        _ = self.client.post('/reviews/new',{'movie_title':'NewMovie', 'user_username':'admin@email.com','review_text':'sff','review_rate':5.4})
        _ = self.client.delete('/users/logout')
        response = self.client.get('/reviews/?movie_title=NewMovie')
        self.assertEqual(response.status_code, 200)
    
