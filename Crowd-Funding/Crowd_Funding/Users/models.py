from django.db import models
from django.utils.timezone import now

# Create your models here.


class profile(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField(default="desciption defualt text")

    def __unicode__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name




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

        def __unicode__(self):
            return self.name

class Projects(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    total_target = models.IntegerField()
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    details = models.TextField()
    user = models.ForeignKey(Register, on_delete=models.CASCADE)

class Featured(models.Model):
    pro = models.ForeignKey(Projects, on_delete=models.CASCADE,related_name="tet")


class Image(models.Model):
    images = models.ImageField(upload_to='media')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, default=None,related_name='image')

    def __unicode__(self):
        return self.name
class reports(models.Model):
    project_id = models.ForeignKey(Projects, related_name="reports", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    report_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.project_id.name, self.Report_name)

class comment(models.Model):
    project_id = models.ForeignKey(Projects,related_name="comment",on_delete=models.CASCADE)
    Comend_name=models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s"%(self.project_id.name,self.Comend_name)



class slider(models.Model):
    slider_name = models.CharField(max_length=200)
    slider_describe = models.TextField()
    slider_img = models.ImageField(verbose_name="photo", upload_to='media', default='default.jpg')


class ProjectsTages(models.Model):
    tags = models.CharField(max_length=50)
    project = models.ForeignKey(Projects,related_name='tag', on_delete=models.CASCADE)

