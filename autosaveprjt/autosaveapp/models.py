from django.db import models

# Create your models here.
class automodel(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    bike=models.CharField(max_length=20)
    text=models.CharField(max_length=20)
    symptoms=models.CharField(max_length=20)
