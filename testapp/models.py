from django.db import models

# Create your models here.

class pune_jobs_tab(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    elegibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField();
    phonenumber=models.IntegerField()


class mumbai_jobs_tab(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    elegibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField();
    phonenumber=models.IntegerField()
