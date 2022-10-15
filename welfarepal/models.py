from distutils.command.upload import upload
from django.db import models
import re
from datetime import date, datetime, time

class DrManager(models.Manager):
    def Doctor_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['firstname']) < 2:
            errors["firstname"] = "first name should be at least 2 characters"


        if len(postData['lastname']) < 2:
            errors["lastname"] = "last name should be at least 2 characters"

        # if not postData['file'] :
        #     errors["certificate"] = "certificate was not uploaded"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        if len(postData['id']) != 8:
            errors["desc"] = "Your ID does not seem to be correct"

        if len(postData['password']) < 8:
            errors["desc"] = "password should be at least 8 characters"

        if postData['password']!=postData['Cpassword']:
            errors["password"] = "Password and its confirmation does not match"
        for E in Doctor.objects.all():
            if postData['email']==E.email:
                errors["DuplicateEmail"]="This Email is Taken"

        return errors

class PatientManager(models.Manager):
    def Patient_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['firstname']) < 2:
            errors["firstname"] = "first name should be at least 2 characters"


        if len(postData['lastname']) < 2:
            errors["lastname"] = "last name should be at least 2 characters"


        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        if len(postData['ID']) != 9:
            errors["desc"] = "Your ID does not seem to be correct"

        if len(postData['password']) < 8:
            errors["desc"] = "password should be at least 8 characters"

        if postData['password']!=postData['Cpassword']:
            errors["password"] = "Password and its confirmation does not match" 
        for E in Patient.objects.all():
            if postData['email']==E.email:
                errors["DuplicateEmail"]="This Email is Taken"  

        return errors



class Doctor(models.Model):
    First_Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    image=models.ImageField(upload_to ='images' , null=True , blank=True)
    Certificate = models.FileField()
    Location = models.CharField(max_length=45)
    Specialization = models.CharField(max_length=45)
    Approval= models.TextField(null=True)
    Experience = models.DateTimeField()
    Phone_Number = models.IntegerField()
    MedicalNumber=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=DrManager()


class Patient(models.Model):
    First_Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    age=models.DateTimeField(null=True)
    Personal_ID = models.CharField(max_length=45)
    Marital_Status = models.CharField(max_length=45)
    Gender = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=PatientManager()


class Profile(models.Model):
    Diagnosis=models.CharField(max_length=45)
    Medicines=models.CharField(max_length=45)
    Description=models.CharField(max_length=45)
    Examinations=models.FileField(upload_to='files/')
    patient = models.ForeignKey(Patient, related_name="profiles", on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="profiles", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Appointments(models.Model):
    vacancies=models.DateTimeField()
    session=models.IntegerField()
    patient = models.ForeignKey(Patient, related_name="appointments", on_delete = models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, related_name="appointments", on_delete = models.CASCADE)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)