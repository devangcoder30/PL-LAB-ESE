from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.EmailField(max_length=50)
    fname=models.CharField(max_length=50)

class Book(models.Model):
    imag=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=200,null=True)
    capt=models.CharField(max_length=300,null=True)
    review=models.CharField(max_length=400,null=True)
