from django.db import models
from tinymce.models import HTMLField
from account.views import User
from django import forms
from ckeditor.fields import RichTextField

# Create your models here.


class blog(models.Model):
    blogTitle = models.CharField(max_length=50, verbose_name= 'Blog Tile')
    blogSubtile = models.TextField(blank=True, null=True, verbose_name= 'Subtitle[if any]')
    featuredImage = models.ImageField(upload_to='images', verbose_name='Featured Image')
    likeCount = models.IntegerField(blank=True, null=True)
    blogBody = RichTextField(blank=True, null=True, verbose_name= 'Body')
    username = models.CharField(max_length=100)
    userPicture = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)
    aboutUser = HTMLField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.blogTitle

    @property
    def get_comments(self):
        return self.comments.all()


class Comment(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(blog, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

'''       
class userComment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=354)
    message = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    time_posted = models.TimeField(auto_now_add=True)
    post = models.ForeignKey(blog , related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + 'made a comment'
    '''