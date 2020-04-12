from django.db import models

# Create your models here.
class contactForm(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject + ' from ' + self.lastName + ' ' + self.firstName


    