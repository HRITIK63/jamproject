from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('admin/',admin.site.urls),
    path('about/',views.about,name='about'),
    path('jobseekerreg/',views.jobseekerreg,name='jobseekerreg'),
    path('employerreg/',views.employerreg,name='employerreg'),
    path('login/',views.login,name='login'),
    path('contact/',views.contact,name='contact'),
    path('jsreg/',views.jsreg,name='jsreg'),
    path('ereg/',views.ereg,name='ereg'),
    path('saveenq/',views.saveenq,name='saveenq'),
    path('validate/',views.validate,name='validate'),
    path('emphome/',views.emphome,name='emphome'),
    path('postjob/',views.postjob,name='postjob'),
    path('manageapp/',views.manageapp,name='manageapp'),
    path('empchengepassword/',views.empchengepassword,name='empchengepassword'),
    path('emplogout/',views.emplogout,name='emplogout'),
    path('pjob/',views.pjob,name='pjob'),
    path('empchengepwd/',views.empchengepwd,name='empchengepwd'),
    path('jobhome/',views.jobhome,name='jobhome'),
    path('applyjob/',views.applyjob,name='applyjob'),
    path('jobchengepassword/',views.jobchengepassword,name='jobchengepassword'),
    path('joblogout/',views.joblogout,name='joblogout'),
    path('jobchengepwd/',views.jobchengepwd,name='jobchengepwd'),
    path('appliedjobs/(?P<id>\d+)',views.appliedjobs,name='appliedjobs'),
    path('jsprofile/(?P<id>\d+)',views.jsprofile,name='jsprofile'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('enquiries/',views.enquiries,name='enquiries'),
    path('jobseekers/',views.jobseekers,name='jobseekers'),
    path('employers/',views.employers,name='employers'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('addnews/',views.addnews,name='addnews'),
    path('deletenews/(?P<id>\d+)',views.deletenews,name='deletenews'),

]
