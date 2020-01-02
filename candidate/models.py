from django.db import models
from home.models import Login,Candidatereg,Companyregistration
from company.models import Vacancy
from django.utils import timezone

# Create your models here.
class Apply(models.Model):
    date = models.DateField(default=timezone.now)
    astatus = models.CharField(max_length=5)
    comp = models.ForeignKey(Companyregistration,on_delete=models.CASCADE)
    cand = models.ForeignKey(Candidatereg, on_delete=models.CASCADE)
    vaca = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

