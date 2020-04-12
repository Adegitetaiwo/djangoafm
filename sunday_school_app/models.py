from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class englishSchoolA(models.Model):
    lessonNumber = models.IntegerField()
    Topic = models.CharField(max_length=100)
    bibleText = models.CharField(max_length=100)
    memoryVerse = models.TextField()
    body = RichTextField()
    source = models.FileField(upload_to='media', max_length=500)
    active = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Enlish Sunday Lesson for Adult'
    def __str__(self):
        return self.Topic

class frenchSchoolA(models.Model):
    lessonNumber = models.IntegerField()
    Topic = models.CharField(max_length=100)
    bibleText = models.CharField(max_length=100)
    memoryVerse = models.TextField()
    body = RichTextField()
    source = models.FileField(upload_to='media', max_length=500)
    active = models.BooleanField()
    class Meta:
        verbose_name_plural = 'French Sunday Lesson for Adult'
    def __str__(self):
        return self.Topic

class yorubaSchoolA(models.Model):
    lessonNumber = models.IntegerField()
    Topic = models.CharField(max_length=100)
    bibleText = models.CharField(max_length=100)
    memoryVerse = models.TextField()
    body = RichTextField()
    source = models.FileField(upload_to='media', max_length=500)
    active = models.BooleanField()
    class Meta:
        verbose_name_plural = 'Yoruba Sunday Lesson for Adult'
    def __str__(self):
        return self.Topic

class englishSchoolI(models.Model):
    lessonNumber = models.IntegerField()
    Topic = models.CharField(max_length=100)
    bibleText = models.CharField(max_length=100)
    memoryVerse = models.TextField()
    body = RichTextField()
    source = models.FileField(upload_to='media', max_length=500)
    active = models.BooleanField()
    class Meta:
        verbose_name_plural = 'Enlish Sunday Lesson for Intermediate'
    def __str__(self):
        return self.Topic

class frenchSchoolI(models.Model):
    lessonNumber = models.IntegerField()
    Topic = models.CharField(max_length=100)
    bibleText = models.CharField(max_length=100)
    memoryVerse = models.TextField()
    body = RichTextField()
    source = models.FileField(upload_to='media', max_length=500)
    active = models.BooleanField()
    class Meta:
        verbose_name_plural = 'French Sunday Lesson for Intermediate'
    def __str__(self):
        return self.Topic

class yorubaSchoolI(models.Model):
    lessonNumber = models.IntegerField()
    Topic = models.CharField(max_length=100)
    bibleText = models.CharField(max_length=100)
    memoryVerse = models.TextField()
    body = RichTextField()
    source = models.FileField(upload_to='media', max_length=500)
    active = models.BooleanField()
    class Meta:
        verbose_name_plural = 'Yoruba Sunday Lesson for Intermediate'
    def __str__(self):
        return self.Topic

class elementarySchool(models.Model):
    lessonNumber = models.IntegerField()
    Topic = models.CharField(max_length=100)
    bibleText = models.CharField(max_length=100)
    memoryVerse = models.TextField()
    body = RichTextField()
    source = models.FileField(upload_to='media', max_length=500)
    active = models.BooleanField()
    class Meta:
        verbose_name_plural = 'Enlish Sunday School Lesson for Elementary'
    def __str__(self):
        return self.Topic