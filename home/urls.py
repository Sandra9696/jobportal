from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name='index'),
    path('', views.mainhome, name='mainhome'),
    path('mainhome', views.mainhome, name='mainhome'),
    path('login', views.login, name='login'),
    path('cansign', views.cansign, name='cansign'),
    path('cmpreg', views.cmpreg, name='cmpreg'),
    path('candidateaction', views.candidateaction, name='candidateaction'),
    path('login', views.login, name='login'),
    path('companyaction', views.companyaction, name='companyaction '),
    path('loginaction', views.loginaction, name='loginaction ')
]