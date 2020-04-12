from django.db import models

# Create your models here.
class userDuty(models.Model):
    userDuty = models.CharField(max_length=50)
    def __str__(self):
        return self.userDuty

class testimony_s(models.Model):
    caption = models.CharField(max_length=100)
    introduction = models.CharField(max_length=2000, blank=True)
    featuredImage = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)
    body = models.TextField()
    username = models.CharField(max_length=50)
    comment = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    userPicture = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, default='static/images/default-avatar.png')
    UserDuty = models.ForeignKey(userDuty, verbose_name='Duty In The Church', on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class firstMinister(models.Model):
    ministerName = models.CharField(max_length=50, verbose_name= "Minister's Name")
    position = models.CharField(max_length=50, verbose_name='Duty in Church')
    picture = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.ministerName

class secondMinister(models.Model):
    ministerName = models.CharField(max_length=50, verbose_name= "Minister's Name")
    position = models.CharField(max_length=50, verbose_name='Duty in Church')
    picture = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.ministerName

class thirdMinister(models.Model):
    ministerName = models.CharField(max_length=50, verbose_name= "Minister's Name")
    position = models.CharField(max_length=50, verbose_name='Duty in Church')
    picture = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.ministerName
