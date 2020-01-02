from django.urls import path
from . import views

urlpatterns = [
    path('adminprofile', views.adminprofile, name='adminprofile'),
    path('adminindex',views.adminindex,name='adminindex'),
    path('viewdetails', views.viewdetails, name='viewdetails'),
    path('candidateupdate/<int:id>', views.candidateupdate, name='candidateupdate'),
    path('companyview', views.companyview, name='companyview'),
    path('logout',views.logout,name='logout'),
    path('companyupdate/<int:id>', views.companyupdate, name='companyupdate'),
    path('deletecan/<int:id>', views.deletecan, name='deletecan'),
    path('deletecmp/<int:id>',views.deletecmp,name='deletecmp'),
    path('vacancyview', views.vacancyview, name='vacancyview'),
    path('moreinfo/<int:id>',views.moreinfo,name='moreinfo'),
    path('vacupdate/<int:id>',views.vacupdate,name='vacupdate'),
    path('deletevac/<int:id>',views.deletevac,name='deletevac')

]