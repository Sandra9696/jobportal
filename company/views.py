from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Login,Candidatereg,Companyregistration
from company.models import Vacancy,Viewcl
from candidate.models import Apply
from django.template import loader
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def companyprofile(request):
    em = request.session.get('email')
    cmp = Companyregistration.objects.filter(cmpemail=em)
    context = {'cmp': cmp}
    return render(request, 'hometemp/companyprofile.html', context)

def companyindex(request):
    return render(request,'hometemp/companyindex.html')

def addvacancy(request):
    em = request.session.get("email")
    cmp = Companyregistration.objects.filter(cmpemail=em)
    context = {'cmp':cmp}
    return render(request,'hometemp/addvacancy.html',context)

def vacancyaction(request):
    if request.method == 'POST':
        vac = Vacancy()
        title = request.POST.get('title')
        description = request.POST.get('description')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        location = request.POST.get('location')
        availability = request.POST.get('availability')
        qualification = request.POST.get('qualification')
        lastdate = request.POST.get('lastdate')
        cmpid= request.POST.get('cid')
        vac.title = title
        vac.description = description
        vac.experience = experience
        vac.skills = skills
        vac.location = location
        vac.availability = availability
        vac.qualification = qualification
        vac.lastdate = lastdate
        vac.cmpreg_id= cmpid
        vac.vacstatus = 0
        vac.save()
        return HttpResponse(" <script> alert ('Vacancy added successfully..wait for approval') ; window.location = '/companyprofile' ; </script> ")

def approvedvac(request):
    em = request.session.get("userid")
    com = Companyregistration.objects.get( cmplogin_id = em )
    vac = Vacancy.objects.filter(cmpreg_id=com,vacstatus=1)
    context = {'vac': vac}
    return render(request, 'hometemp/approvedvac.html', context)

def moreinfocan(request,id):
    va = Vacancy.objects.filter(id = id)
    context = {'va': va}
    return render(request, 'hometemp/moreinfocan.html', context)

def appliedvac(request):
    em = request.session.get("userid")
    com = Companyregistration.objects.get( cmplogin_id = em )
    appl = Apply.objects.filter(comp_id = com, astatus=0)
    context = {'appl': appl}
    return render(request, 'hometemp/appliedvac.html', context)

def more(request,id):
    ap = Apply.objects.filter(id = id)
    context = {'ap': ap}
    return render(request, 'hometemp/more.html', context)

def sendcl(request,id):
    updt = Apply.objects.get(id=id)
    updt.astatus = 1
    email=updt.cand.email
    updt.save()
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            cl = Viewcl()
            cl.subject = subject
            cl.message = message
            ap = request.POST.get('aid')
            cn = request.POST.get('cid')
            cl.vacan = ap
            cl.cand_id=cn
            cl.save()
            to = email
            res = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])
            return HttpResponse("<script>alert('Accepted ...Check your mail');window.location ='/appliedvac';</script>")
    return render(request, "hometemp/sendcl.html", {'form': form,'updt':updt})

def deletecl(request,id):
    dele = Apply.objects.get( id = id )
    dele.delete()
    return HttpResponseRedirect('../appliedvac')










