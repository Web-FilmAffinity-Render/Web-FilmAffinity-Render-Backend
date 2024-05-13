from django.db import models


class User(models.Model):

    name = models.CharField(max_length=256)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        
        super().save(*args, **kwargs)