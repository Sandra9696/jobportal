from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Login,Candidatereg,Companyregistration
from django.template import loader
# Create your views here.
def index(request):
    #return HttpResponse('Welcome')
    return render(request,'hometemp/mainhome.html')

def about(request):
    return render(request,'hometemp/about.html')

def mainhome(request):
    return render(request,'hometemp/mainhome.html')

def login(request):
    return render(request,'hometemp/login.html')

def cansign(request):
    return render(request,'hometemp/cansign.html')

def cmpreg(request):
    return render(request,'hometemp/cmpreg.html')

def candidateaction (request):
    #return HttpResponse("Registration Form")
    if request.method =='POST':
        log = Login()
        email = request.POST.get('email')
        password = request.POST.get('password')
        log.email = email
        log.password = password
        log.category = "candidate"
        log.status = 0
        log.save()

        reg=Candidatereg()
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        state = request.POST.get('state')
        gender = request.POST.get('gender')
        qualification = request.POST.get('qualification')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        skills = request.POST.get('skills')
        resume = request.FILES.get('resume')
        reg.name = name
        reg.age = age
        reg.address = address
        reg.state = state
        reg.gender = gender
        reg.qualification = qualification
        reg.mobile = mobile
        reg.email = email
        reg.password = password
        reg.skills = skills
        reg.resume = resume
        reg.status = 0
        reg.canlogin = log
        reg.save()
        return HttpResponse(" <script> alert ('Thankyou for Registration') ; window.location = '/cansign' ; </script> ")

def companyaction (request):
    #return HttpResponse("Registration Form")
    if request.method =='POST':
        log = Login()
        email = request.POST.get('cmpemail')
        password = request.POST.get('cmppassword')
        log.email = email
        log.password = password
        log.category = "company"
        log.status = 0
        log.save()

        reg = Companyregistration()
        cmpname = request.POST.get('cmpname')
        cmpemail = request.POST.get('cmpemail')
        cmpregisterid = request.POST.get('cmpregisterid')
        cmpaddress = request.POST.get('cmpaddress')
        cmpstate = request.POST.get('cmpstate')
        cmpmobile = request.POST.get('cmpmobile')
        cmpdescription = request.POST.get('cmpdescription')
        cmpusername = request.POST.get('cmpusername')
        cmppassword = request.POST.get('cmppassword')
        cmpowner = request.POST.get('cmpowner')
        reg.cmpname = cmpname
        reg.cmpemail = cmpemail
        reg.cmpregisterid = cmpregisterid
        reg.cmpaddress = cmpaddress
        reg.cmpstate = cmpstate
        reg.cmpmobile = cmpmobile
        reg.cmpdescription = cmpdescription
        reg.cmpusername = cmpusername
        reg.cmppassword = cmppassword
        reg.cmpowner = cmpowner
        reg.cmpstatus = 0
        reg.cmplogin = log
        reg.save()
        return HttpResponse(" <script> alert ('Thankyou for Registration') ; window.location = '/cmpreg' ; </script> ")

def loginaction(request):
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            if (Login.objects.filter(email=email, password=password).exists()):  # Email is given in db
                logins = Login.objects.filter(email=email, password=password)

                for login in logins:
                    usertype = login.category
                    status = login.status
                    request.session['usertype'] = usertype

                    if (usertype == 'admin'):
                        request.session['email'] = login.email  # request.session['arrayname'] = login.dbcolumn name
                        request.session['password'] = login.password
                        request.session['usertype'] = usertype
                        request.session["userid"] = login.pk
                        request.session['status'] = login.status
                        return HttpResponseRedirect('adminprofile')

                    elif ((usertype=='candidate')&(status == '1')):
                        request.session['email'] = login.email  # request.session['arrayname'] = login.dbcolumn name
                        request.session['password'] = login.password
                        request.session['usertype'] = usertype
                        request.session["userid"] = login.pk
                        return HttpResponseRedirect('candidateprofile')

                    elif ((usertype == 'company')&(status == '1')):
                        request.session['email'] = login.email  # request.session['arrayname'] = login.dbcolumn name
                        request.session['password'] = login.password
                        request.session['usertype'] = usertype
                        request.session["userid"] = login.pk
                        return HttpResponseRedirect('companyprofile')

                    else:
                        template = loader.get_template('hometemp/login.html')
                        context = {'error': 'Incorrect username or password' }  # context is a dictionary
                        #return HttpResponse(template.render(context, request))
                        return HttpResponse("<script>alert('Wait for admin approval');window.location ='/login';</script>")

            else:
                template = loader.get_template('hometemp/login.html')
                context = {'error': 'Incorrect information'}
                return HttpResponse("<script>alert('Incorrect username or password');window.location ='/login';</script>")

        else:
            template = loader.get_template('hometemp/login.html')
            context = {}
            return HttpResponse("<script>alert('Cannot login');window.location ='/login';</script>")










