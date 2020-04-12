from django.db import models

# Create your models here.

class videos(models.Model):
    sourceLink = models.URLField(max_length=500)
    title = models.CharField(max_length=50)
    featuredImage = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)
    minister = models.CharField(max_length=70)
    class Meta:
        verbose_name_plural = 'Videos'
    def __str__(self):
        return self.title
    