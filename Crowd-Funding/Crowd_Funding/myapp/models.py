from django.db import models
from django.utils.timezone import now
from taggit.managers import TaggableManager
from static import images
# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField(default="desciption defualt text")

    def __unicode__(self):
        return self.name
class project(models.Model):
    name=models.CharField(max_length=120,unique=True)
    description = models.TextField(default="desciption defualt text")
    coverimage=models.ImageField(upload_to='images')
    image1=models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    category=models.CharField(max_length=25,null=True)
    timestamp = models.DateTimeField(default=now, blank=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "imageupload"