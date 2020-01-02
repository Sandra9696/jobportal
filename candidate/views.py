from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.models import Login,Candidatereg,Companyregistration
from company.models import Vacancy,Viewcl
from candidate.models import Apply
from django.utils import timezone
# Create your views here.
def candidateprofile(request):
    em = request.session.get('email')  # fetch the mail of a single user
    pro = Candidatereg.objects.filter(email=em)  # filter() is used to filter the emailid from the database
    context = {'pro1': pro}  # prof that is key is given in the profile table
    return render(request, 'hometemp/candidateprofile.html', context)

def candidateindex(request):
    return render(request,'hometemp/candidateindex.html')

def candidatevacview(request):
    #vac = Vacancy.objects.filter(vacstatus = 1)
    em = request.session.get('userid')
    can = Candidatereg.objects.filter(canlogin_id=em)
    vac=Vacancy.objects.filter(skills__in=can.values_list('skills',flat=True),vacstatus=1)
    context = {'vac':vac}
    return render(request,'hometemp/candidatevacview.html',context)

def candidatemoreinfo(request,id):
    va = Vacancy.objects.filter(id=id)
    context = {'va': va}
    return render(request, 'hometemp/candidatemoreinfo.html', context)

def candidateapply(request,id):
    em = request.session.get('userid')
    can = Candidatereg.objects.get(canlogin_id=em)
    vac = Vacancy.objects.get(id=id)
    ap = Apply.objects.filter(vaca_id=vac,cand_id=can)
    dt = timezone.now()
    dat = vac.lastdate
    dm = dt.strftime('%Y-%m-%d')
    if(ap.exists()):
        return HttpResponse("<script>alert('Already applied');window.location ='/candidatevacview';</script>")
    elif(dm>=dat):
        return HttpResponse("<script>alert('Job expired');window.location ='/candidatevacview';</script>")
    else:
        context = {'can':can,'vac':vac}
        return render(request,'hometemp/candidateapply.html',context)

def applyaction(request):
    if request.method == 'POST':
        ap = Apply()
        compn = request.POST.get("cid")
        va = request.POST.get("vid")
        candid = request.POST.get("canid")
        ap.astatus = 0
        ap.comp_id = compn
        ap.vaca_id = va
        ap.cand_id = candid
        ap.save()
        return HttpResponse(" <script> alert ('Successfully applied') ; window.location = '/candidatevacview' ; </script> ")

def applistatus(request):
    em = request.session.get('userid')
    can = Candidatereg.objects.get(canlogin_id=em)
    ap =Apply.objects.filter(cand_id=can,astatus=1)
    context = {'ap':ap}
    return render(request,'hometemp/applistatus.html',context)

def callletter(request,id):
    vi = Viewcl.objects.get(vacan=id)
    context = {'vi': vi}
    return render(request, 'hometemp/callletter.html', context)





