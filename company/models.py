from django.db import models
from home.models import Login,Candidatereg,Companyregistration

# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    experience = models.CharField(max_length=15)
    skills = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    availability = models.CharField(max_length=10)
    qualification = models.CharField(max_length=20)
    lastdate = models.CharField(max_length=20)
    vacstatus = models.IntegerField()
    cmpreg = models.ForeignKey(Companyregistration,on_delete=models.CASCADE)

class Viewcl(models.Model):
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=50)
    vacan = models.CharField(max_length=5)
    cand = models.ForeignKey(Candidatereg,on_delete=models.CASCADE)

