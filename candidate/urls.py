from django.urls import path
from . import views

urlpatterns = [
    path('candidateprofile', views.candidateprofile, name='candidateprofile'),
    path('candidateindex',views.candidateindex,name='candidateindex'),
    path('candidatevacview',views.candidatevacview,name='candidatevacview'),
    path('candidatemoreinfo/<int:id>',views.candidatemoreinfo,name='candidatemoreinfo'),
    path('candidateapply/<int:id>',views.candidateapply,name='candidateapply'),
    path('candidateapply/applyaction',views.applyaction,name='applyaction'),
    path('applistatus', views.applistatus, name='applistatus'),
    path('callletter/<int:id>',views.callletter,name='callletter')

]