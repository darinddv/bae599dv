from django.db import models

# Create your models here.

class LocationLoads(models.Model):
    location_name = models.CharField(max_length=50)
    batteries = models.JSONField()
    loads = models.JSONField()

    def __str__(self):
        return f'{self.location_name} ({self.loads})'