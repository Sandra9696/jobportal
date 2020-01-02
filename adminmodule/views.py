from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Login,Candidatereg,Companyregistration
from company.models import Vacancy
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def adminprofile(request):
    return render(request,'hometemp/adminprofile.html')

def adminindex(request):
    return render(request,'hometemp/adminindex.html')

def viewdetails(request):
    can = Candidatereg.objects.filter(status = 0)  # to fetch details of all users all() is used
    context = {'can': can}
    return render(request, 'hometemp/viewdetails.html', context)

def companyview(request):
    cm = Companyregistration.objects.filter(cmpstatus = 0)  # to fetch details of all users all() is used
    context = {'cm': cm}
    return render(request, 'hometemp/companyview.html', context)

def candidateupdate(request,id):
    updt = Candidatereg.objects.get(canlogin_id=id)
    updt.status = 1
    updt.save()
    up = Login.objects.get(id=id)
    up.status = 1
    up.save()
    subject = "Accept jobportal login"
    msg = "Request has been accepted.please go to this  http://127.0.0.1:8000/  for login our website"
    to = updt.email
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    return HttpResponse("<script>alert('Accepted ...Check your mail');window.location ='/viewdetails';</script>")

def companyupdate(request,id):
    up = Companyregistration.objects.get( cmplogin_id = id )
    up.cmpstatus = 1
    up.save()
    uplog = Login.objects.get( id = id )
    uplog.status = 1
    uplog.save()
    subject = "Accept jobportal login"
    msg = "Request has been accepted.please go to this  http://127.0.0.1:8000/  for login our website"
    to = up.cmpemail
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    return HttpResponse("<script>alert('Accepted ...Check your mail');window.location ='/companyview';</script>")

def deletecan(request,id):
    dele = Candidatereg.objects.get( canlogin_id = id )
    dele.delete()
    logdel = Login.objects.get(id=id)
    logdel.delete()
    return HttpResponseRedirect('../viewdetails')

def deletecmp(request,id):
    dele = Companyregistration.objects.get( cmplogin_id = id )
    dele.delete()
    logdel= Login.objects.get(id=id)
    logdel.delete()
    return HttpResponseRedirect('../companyview')

def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return HttpResponse(' <script> alert("you are successfully Logged off.."); window.location ="/login"; </script>')

def vacancyview(request):
    vac = Vacancy.objects.filter( vacstatus = 0 )
    context = {'vac': vac}
    return render(request, 'hometemp/vacancyview.html', context)

def moreinfo(request,id):
    va = Vacancy.objects.filter(id = id)
    context = {'va': va}
    return render(request, 'hometemp/moreinfo.html', context)

def vacupdate(request,id):
    vac1 = Vacancy.objects.get( id = id )
    vac1.vacstatus = 1
    vac1.save()
    return HttpResponseRedirect('../vacancyview')
    #subject = "Accept jobportal login"
    #msg = "Request has been accepted.please go to this  http://127.0.0.1:8000/  for login our website"
    #to = up.cmpemail
    #res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    #return HttpResponse("<script>alert('Accepted ...Check your mail');window.location ='/companyview';</script>")

def deletevac(request,id):
    dele = Vacancy.objects.get( id = id )
    dele.delete()
    return HttpResponseRedirect('../vacancyview')












