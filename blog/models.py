from django.db import models
from django.contrib.auth.models import User
from  . helpers import *
from tinymce.models import HTMLField


# Create your models here.

# --------------------------------------------------------------------------------------------------

class BlogModel(models.Model):
    
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description=models.CharField(max_length=300,default="")
    content = HTMLField(default="")
    slug = models.SlugField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug =generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)
        
# ---------------------------------------------------------------------------------------------------

class Query(models.Model):

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    phone=models.IntegerField(default="")
    query=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name +" "+ self.last_name      

# ---------------------------------------------------------------------------------------------------
