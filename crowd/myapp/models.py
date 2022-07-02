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

class Register(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        email = models.EmailField(max_length=50, unique=True)
        password = models.BinaryField(max_length=200)
        phone = models.CharField(max_length=11, unique=True, null=True)
        is_active = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)
        profile_img = models.ImageField(verbose_name="photo", upload_to='media', default='default.jpg')
        birthdate = models.DateField(null=True)
        facebook_profile = models.URLField(null=True)
        country = models.CharField(max_length=30, null=True)
        last_login = models.DateTimeField(null=True)

