from django.db import models
from datetime import datetime

# Create your models here.
class liveForcast(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.TextField(default=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    watching = models.IntegerField()
    image = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)
    source = models.URLField(max_length=500)
    active = models.BooleanField()

    def __str__(self):
        return self.title