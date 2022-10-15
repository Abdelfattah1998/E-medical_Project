from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.frontpage),
    path('home' ,views.home),
    path('reg' , views.LogOrReg),
    path('contactUs' , views.Us),
    path('regestire1' , views.regPatient),
    path('regestire2' , views.regDoc),
    path('DoctorDash/<id>' , views.DoctorDash),
    path('patientDash/<id>' , views.PatientDash),
    path('login' , views.logDocAndPatient),
    path('logoutPatient' , views.logoutP),
    path('logoutDoctor' , views.logoutD),
    path('specialization/<special>' ,views.Showspecialization),
    path('specialization/<special>/Assign' ,views.specialization),
    # path('DoctorDash/show/<int:id>',views.show),
    path('DoctorDash/update/<int:id>',views.update),
    path('update_patient/<id>',views.update_patient),
    path('CheckBox/<id>', views.index),
    path('CheckBox/book/<id>', views.book),
    path('Back/<id>',views.back),
    path('patientbook/<id>/<special>' , views.patientbook),
    path('Add/<drid>/<id>/<special>' , views.addpatientapp),
    path('backSpec/<special>' , views.Showspecialization),
    path('patientDash/cancel/<int:id>', views.cancel, name='delete'),
    path('DoctorDash/show/<id>' , views.profileview),
    path('patientDash/show/<id>' ,views.profileviewPatien),
    path('DoctorDash/show/DoctorDash/<id>' , views.Back),
    # path('Add/<id>' , views.AddNew),
    path('Admin' , views.Admin),
    path('approval/<id>' , views.Approval),
    path('reject/<id>' , views.Reject),
    path('notAproval' , views.NotApproval),
    
    
   
]