from django.db import models

# Create your models here.
class displaySilder(models.Model):
    title = models.CharField(max_length=150)
    discriptionTop = models.CharField(blank = True, null=True, max_length=40)
    discriptionBottom = models.CharField(blank = True, null=True, max_length=100)
    displayImage = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title
    

class setCountdownDate(models.Model):
    eventTitle = models.CharField(max_length=100)
    eventDate = models.DateField()
    eventDiscription = models.TextField()
    endTimeMessage = models.CharField(max_length=100)
    Active = models.BooleanField()

    def __str__(self):
        return self.eventTitle

class userType(models.Model):
    createUserType = models.CharField(max_length=50, verbose_name= 'User Title')

    def __str__(self):
        return self.createUserType

class urgentMessage(models.Model):
    messageTitle =  models.CharField(max_length=50, verbose_name= 'Message Title')
    Active = models.BooleanField()
    UserTitle = models.ForeignKey(userType, verbose_name= "User Title", on_delete=models.CASCADE)
    userImage = models.ImageField(upload_to='images', verbose_name= 'User Passport(with any background')
    date = models.DateTimeField(auto_now_add=True)
    likeCount = models.IntegerField(verbose_name= 'Likes Count')
    messageBody = models.TextField(verbose_name= 'Message Body')

    def __str__(self):
        return self.messageTitle

class sermonUpdate(models.Model):
    link = models.URLField(max_length=500, verbose_name= 'Link to Video Source (e.g Youtube.)')
    image = models.ImageField(upload_to='images', verbose_name= 'Image of a Scene During The Service')
    sermonTitle = models.CharField(max_length=100, verbose_name='Sermon Title')
    precherName = models.CharField(max_length=70, verbose_name='Officiating Minister')

    def __str__(self):
        return self.sermonTitle + ' by ' + self.precherName

class event(models.Model):
    theme = models.CharField(max_length=150)
    bible_ref = models.TextField()
    date =  models.CharField(max_length=50)
    detail = models.TextField()
    active = models.BooleanField()
    
    def __str__(self):
        return self.theme
    
class subcribe(models.Model):
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email