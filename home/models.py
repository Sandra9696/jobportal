from django.db import models
# Create your models here.
class Login(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    category = models.CharField (max_length = 20)
    status = models.CharField (max_length = 20)

class Candidatereg(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    qualification = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    skills = models.CharField(max_length=20)
    resume = models.FileField(upload_to ='fileup')
    status = models.CharField (max_length = 20)
    canlogin = models.ForeignKey(Login,on_delete=models.CASCADE)

class Companyregistration(models.Model):
    cmpname = models.CharField(max_length=20)
    cmpemail = models.CharField(max_length=30)
    cmpregisterid = models.CharField(max_length=20)
    cmpaddress = models.CharField(max_length=50)
    cmpstate = models.CharField(max_length=10)
    cmpmobile = models.CharField(max_length=10)
    cmpdescription = models.CharField(max_length=10)
    cmpusername = models.CharField(max_length=20)
    cmppassword = models.CharField(max_length=20)
    cmpowner = models.CharField(max_length=20)
    cmpstatus = models.CharField (max_length = 20)
    cmplogin = models.ForeignKey(Login,on_delete=models.CASCADE)


