from django.db import models

# Create your models here.
class adminSignup(models.Model):
    full_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password=models.CharField(max_length=30)
