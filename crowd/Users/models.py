from django.db import models
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 50 , unique=True)
    password = models.BinaryField(max_length = 200)
    phone = models.CharField(max_length = 11 , unique=True, null=True)
    is_active = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    profile_img = models.ImageField(verbose_name="photo", upload_to='media' ,default='default.jpg')
    birthdate = models.DateField(null = True)
    facebook_profile = models.URLField(null = True)
    country = models.CharField(max_length = 30 , null = True)
    last_login = models.DateTimeField(null=True)
