from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blackhole(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item_name = models.CharField(max_length=255)
    item_dump = models.TextField()
    item_image = models.ImageField(null=True)