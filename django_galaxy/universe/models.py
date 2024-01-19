from django.db import models
from Blackhole.models import Blackhole

class Universe(models.Model):
    name = models.CharField(max_length=256)

class Galaxy(models.Model):
    name = models.CharField(max_length=255)
    universe_name_id = models.ForeignKey(Universe, on_delete=models.CASCADE, null=True)
    size = models.IntegerField()
    dark_matter = models.BooleanField()
    star_count = models.IntegerField()
    center = models.ForeignKey(Blackhole, on_delete=models.CASCADE)
    Collision_time = models.IntegerField()

class SolarSystem(models.Model):
    name = models.CharField(max_length=255)
    galaxy_id = models.ForeignKey(Galaxy, on_delete=models.CASCADE, null=True)
    number_of_planets = models.IntegerField()
    number_of_stars = models.IntegerField()


class Planet(models.Model):
    name = models.CharField(max_length=255)
    solar_system_id = models.ForeignKey(SolarSystem, on_delete=models.CASCADE, null=True)
    size = models.IntegerField()
    habitable = models.BooleanField()
    lowest_temperature = models.IntegerField()
    highest_temperature = models.IntegerField()
    gravity = models.IntegerField()
