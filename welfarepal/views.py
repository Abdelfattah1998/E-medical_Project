from asyncio.windows_events import NULL
from multiprocessing import context
from tokenize import Special
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages 
from .models import *
import bcrypt
from datetime import datetime, timedelta
import calendar
from django.http import JsonResponse,HttpResponse
import json

def frontpage(request):
    return render(request,"MainPage.html")

def Approval(request , id):
    doctor = Doctor.objects.get(id=id)
    doctor.Approval='Yes'
    doctor.save()
    return redirect ('/Admin')


def Reject(request , id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect ('/Admin')

def NotApproval(request):
    return render (request,'NotApproval.html')
    
def Admin (request):
    context ={
            'AllDoctors' : Doctor.objects.all(),
        }
    return render (request ,'Admin.html' ,context)

def logDocAndPatient(request):
    email=request.POST['email']
    password=request.POST['password']
    if email == "Admin@gmail.com":
        patient=Patient.objects.get(email = request.POST['email'])
        if bcrypt.checkpw(password.encode(), patient.password.encode()): #patient.password == password:
                request.session['fname']=patient.First_Name
                request.session['reglog']=False #False indicates login while True indicates Register
                request.session['patientid']=patient.id
                id=request.session['patientid']
                return redirect ('/Admin')
        else:
                messages.error(request,"password is not valid")
                return redirect ('/reg')
    if Doctor.objects.filter(email = email):
            doctor=Doctor.objects.get(email = request.POST['email'])
            doctor=Doctor.objects.get(email = request.POST['email'])
            if doctor.Approval== None:
                return redirect ('/notAproval')

            if bcrypt.checkpw(password.encode(), doctor.password.encode()): #dr.password == password:
                request.session['fname']=doctor.First_Name
                request.session['reglog']=False #False indicates login while True indicates Register
                request.session['drid']=doctor.id
                id=request.session['drid']
                return redirect("/DoctorDash/" +str(id))
            else:
                messages.error(request,"password is not valid")
                return redirect ('/reg')
    elif Patient.objects.filter(email = email):
            patient=Patient.objects.get(email = request.POST['email'])
            if bcrypt.checkpw(password.encode(), patient.password.encode()): #patient.password == password:
                request.session['fname']=patient.First_Name
                request.session['reglog']=False #False indicates login while True indicates Register
                request.session['patientid']=patient.id
                id=request.session['patientid']
                return redirect("/patientDash/" + str(id))
            else:
                messages.error(request,"password is not valid")
                return redirect ('/reg')
    else:
        messages.error(request,"email is not found")
        return redirect("/reg")
  
def DoctorDash(request ,id):
    if 'drid' in request.session :
        ThisDoctor = Doctor.objects.get(id=id)
        context = {
            'DocName' : ThisDoctor.First_Name ,
            'ThisDoctorApp' : ThisDoctor.appointments.all(),
            'DocSPICE' : ThisDoctor.Specialization ,
            'thisDoctor' : ThisDoctor,
            'image' : ThisDoctor.image
        }
        
        return render (request,'doctor_dashboard.html' ,context)
    else : 
        return redirect ('/reg')

def PatientDash (request , id):
    if 'patientid' in request.session:
        ThisPattient = Patient.objects.get(id=id)
        context = {
            'PattientName' : ThisPattient.First_Name ,
            'ThisPattient' : ThisPattient,
            'ThisPattientApp' : ThisPattient.appointments.all()

        }
        return render (request , 'patient_dashboard.html' , context)
    else :
        return redirect ('/reg')

def regPatient(request):
    errors = Patient.objects.Patient_validator(request.POST)
    email=request.POST['email'] 
    # if Patient.objects.filter(email = email):
    #     errors['email1'] = "already existed email address!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request , 'LoginAndReg.html')
    
    else :
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        Email = request.POST['email']
        id=request.POST['ID']
        Age=request.POST['age']
        Gender=request.POST['gender']
        Status=request.POST['marital']
        password=request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        request.session['fname']= firstname
        request.session['reglog']= True
        patient=Patient.objects.create(First_Name=firstname , Last_Name=lastname ,password=pw_hash , email=Email , Personal_ID =id, age=Age,
        Marital_Status = Status , Gender = Gender )
        request.session['patientid']= patient.id
        id=request.session['patientid']
        return redirect("/patientDash/"+str(id))


def regDoc(request):
    errors = Doctor.objects.Doctor_validator(request.POST)
    email=request.POST['email'] 
    # if Doctor.objects.filter(email = email):
    #     errors['email1'] = "already existed email address!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request , 'LoginAndReg.html')
    
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    password=request.POST['password'] 
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    Email = request.POST['email']
    image=request.FILES['image']
    Certificate=request.FILES['file']
    Location=request.POST['Location']
    Specialization=request.POST['Specilization']
    MedicalNumber=request.POST['id']
    Experience=request.POST['Experience']
    Phone_Number=request.POST['Phonenumber']
    request.session['fname']= firstname
    request.session['reglog']= True
    thisDoctor=Doctor.objects.create(First_Name=firstname,Last_Name=lastname,email=Email,password=pw_hash
    ,MedicalNumber=MedicalNumber,Certificate=Certificate,Location=Location,Specialization=Specialization,Experience=Experience,Phone_Number=Phone_Number, image=image)
    request.session['drid']= thisDoctor.id
    id=request.session['drid']
    return redirect("/notAproval")


def appointments(request):
    thisdoctor=Doctor.objects.get(id=request.session['drid'])
    myappointments=appointments.objects.filter(doctor=thisdoctor)
    context={
        'myappointments':myappointments
    }
    return render(request,"dr_dashboard.html",context)

def pappointments(request):
    thispatient=Patient.objects.get(id=request.session['patientid'])
    myappointments=appointments.objects.filter(patient=thispatient)
    context={
        'myappointments':myappointments
    }
    return render(request,"patient_dashboard.html",context) 


def cancel(request,id):
    pattient = Patient.objects.get(id=request.session['patientid'])
    cancel = pattient.appointments.get(id=id)
    cancel.patient=None
    cancel.save()
    return JsonResponse ({'success': True, 'message': 'Delete','id':id})




def profile(request,id):
    thisdoctor=Doctor.objects.get(id=request.session['drid'])
    drs=Doctor.objects.filter(Specialization=thisdoctor.Specialization)
    thispatient=Patient.objects.get(id=id)
    profile=thispatient.Profile.filter(doctor=drs)    #We used a filter based on array of doctors with specific specialization error might happen
    context={
        'profile':profile
    }
    return render(request,"patientprofile.html",context)


def home (request):
    return render (request , 'home.html')
def LogOrReg (request):
    return render (request , 'LoginAndReg.html')
def Us(request):
    return render (request , 'Us.html')




def logoutP (request) :
    del request.session['patientid']
    return redirect ('/')
def logoutD (request) :
    del request.session['drid']
    return redirect ('/')

def retrun_main_home(request):
    return redirect('/')


def Showspecialization(request,special):
    alldoctors=Doctor.objects.all()  
    if request.session['location'] :
        doctors=Doctor.objects.filter(Specialization=special,Location=request.session['location'])
    else:
        doctors=Doctor.objects.filter(Specialization=special)
    location=[]
    for doctor in alldoctors:
        if doctor.Location not in location:
            location.append(doctor.Location)
    
    context={
        'drs': doctors,
        'locations': location,
        'thisSpecial' : special,
    }
    return render (request,"specialize.html",context)


def specialization(request,special):
    if request.POST:
        request.session['location']=request.POST['location']
    return redirect('/specialization/'+str(special))

def show(request,id):
    
    context={
        'patient':Patient.objects.get(id = int(id))
    }
    return render (request,'show.html',context)

def update(request,id):
    context={
        'patient':Patient.objects.get(id = int(id)),
        'thisDoctor':Doctor.objects.get(id=request.session['drid'])
    }
    return render (request,'update.html',context)

def update_patient(request,id):
    patient = Patient.objects.get(id = int(id))
    thisdoctor=Doctor.objects.get(id=request.session['drid'])
    Diagnosis = request.POST['diagnosis']
    Description = request.POST['description']
    Medicines = request.POST['medicines']
    Examinations = request.FILES['examinations']
    Profile.objects.create(Diagnosis=Diagnosis, Medicines=Medicines,Description=Description,Examinations=Examinations,patient=patient,doctor=thisdoctor)
    return redirect('/DoctorDash/show/'+ str(id))

def book(request ,id):
    doctor = Doctor.objects.get(id=id)
    if request.POST:
        vacancies=request.POST.getlist('vacancies')
        print(vacancies)
    for vacancy in vacancies:
        Time =vacancy.split(',')
        x=int(Time[0])#where x is the day from today
        y=int(Time[1])#y is the time slots from 8 to 17
        day=(datetime.today())+timedelta(days=x)
        Appointments.objects.create(vacancies=datetime.date(day),session=y , doctor=doctor)
    context = {
        'today':datetime.today().weekday
    } 
    return redirect("/CheckBox/" + str(id))


def index(request , id):
    today=datetime.today().weekday()
    print("today+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(today)
    ranger=range(today,7)
    ThisDoctor = Doctor.objects.get(id=id)
    context = {
        'range':ranger ,
        'hours':range(8,18),
        'DocName' : ThisDoctor.First_Name ,
        'thisDoc' :ThisDoctor
    }
    return render(request,"doctorcal.html",context)


def back (request,id ) :
    return redirect ('/DoctorDash/' + str(id))


def patientbook(request ,id , special):
    if 'patientid' in request.session:
        doctor = Doctor.objects.get(id=id)
        thispatient=Patient.objects.get(id=request.session['patientid'])
        appointments=Appointments.objects.filter(doctor=doctor)
        
        vacanciess=[]
        for appointment in appointments:
            if appointment.vacancies not in vacanciess:
                vacanciess.append(appointment.vacancies)
        # dates=appointments.vacancies
        sessions=[[]]
        n=0
        for date in vacanciess:
            sessions.append([])
            for s in (Appointments.objects.filter(vacancies=date)):
                if s not in sessions[n] and s in doctor.appointments.all() and not s.patient:    
                    sessions[n].append(s)
            sessions[n].insert(0,date)
            n += 1
        context={
            'sessions':sessions,
            'drid':id,
            'thisSpecial' : special,
            'thispattient' : Patient.objects.get(id=request.session['patientid'])
        }
        return render(request,"patientapp.html",context)
    else : 
        return redirect ('/reg')


def addpatientapp(request,drid,id , special):
    thisapp=Appointments.objects.get(id=int(id))
    thispatient=Patient.objects.get(id=request.session['patientid'])
    thisapp.patient=thispatient
    thisapp.save()
    return redirect("/patientbook/"+str(drid) +'/' +str(special))


def profileview(request,id):
    thisdoctor=Doctor.objects.get(id=request.session['drid'])
    thispatient=Patient.objects.get(id=id)
    patient_profile=Profile.objects.filter(doctor__Specialization=thisdoctor.Specialization,patient=thispatient)
    context={
        'patient_profile':patient_profile,
        'thispatient':thispatient,
        'thisDoctor': thisdoctor,
    }
    return render(request,"PatientProfile.html",context)


def Back(request,id):
    return redirect ('/DoctorDash'+str(id))


def profileviewPatien(request,id):
    thispatient=Patient.objects.get(id=request.session['patientid'])
    patient_profile=Profile.objects.all().order_by('created_at')
    context={
        'patient_profile':patient_profile,
        'thispatient':thispatient,
    }
    return render(request,"PatientProfileforPatient.html",context)







