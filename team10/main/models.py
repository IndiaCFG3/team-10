from django.db import models

# Create your models here.
class adminSignup(models.Model):
    full_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password=models.CharField(max_length=30)
class userSignup(models.Model):
    full_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password=models.CharField(max_length=30)
    university=models.CharField(max_length=100)
class courses(models.Model):
    coursename=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    videolink=models.CharField(max_length=500)
    pdfdrivelink=models.CharField(max_length=1000)
    category=models.CharField(max_length=50)