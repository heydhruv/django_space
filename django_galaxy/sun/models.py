from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    email_id = models.EmailField()
    address = models.TextField(max_length=255)
    image = models.ImageField()
