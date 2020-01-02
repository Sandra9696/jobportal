from django.urls import path
from . import views

urlpatterns = [
    path('companyprofile', views.companyprofile, name='companyprofile'),
    path('addvacancy', views.addvacancy, name='addvacancy'),
    path('vacancyaction', views.vacancyaction, name='vacancyaction'),
    path('approvedvac',views.approvedvac,name='approvedvac'),
    path('companyindex', views.companyindex, name='companyindex'),
    path('appliedvac', views.appliedvac, name='appliedvac'),
    path('moreinfocan/<int:id>', views.moreinfocan, name='moreinfocan'),
    path('more/<int:id>', views.more, name='more'),
    path('sendcl/<int:id>', views.sendcl, name='sendcl'),
    path('deletecl/<int:id>',views.deletecl,name='deletecl')

]