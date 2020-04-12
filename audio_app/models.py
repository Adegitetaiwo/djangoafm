from django.db import models
from datetime import datetime

# Create your models here.
class audios(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default = datetime.now, blank=True, verbose_name='Date and Time')
    listeners = models.IntegerField(default = 0, blank=True)
    source = models.URLField(max_length=200)
    active = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Audios'
    def __str__(self):
        return self.title

