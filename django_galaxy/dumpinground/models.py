from django.db import models

class Dump(models.Model):
    """A dump of a database."""
    name = models.CharField(max_length=256, unique=True)  # The name of the dump
    data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
