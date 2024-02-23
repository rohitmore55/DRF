from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    title=models.CharField(max_length=30,blank=False,null=False)
    body=models.CharField(max_length=300,blank=False,null=False)
    summary=models.CharField(max_length=60,blank=False,null=False)
    doc=models.FileField(upload_to='pdf/')
    cat=[('News',"News"),('Announcement',"Announcement"),('Post',"post")]
    catagory=models.CharField(max_length=30,choices=cat)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='contents')



