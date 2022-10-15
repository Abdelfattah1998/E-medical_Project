# **IPEKYOLU** 

## Table of Contents
* [Run Localy](#run-localy)
* [Abstract](#abstract)
* [Main Page](#main-page)
* [Home Page](#home-page)
* [Contact Us Page](#contact-us-page)
* [Login and Registration](#login-and-registration)
* [Doctor Dashboard Page](#doctor-dashboard-page)
* [Patient Dashboard Page](#patient-dashboard-page)
* [CheckBox Page](#checkbox-page)
* [Update Page](#update-page)
* [Patient Diagnosis Page](#patient-diagnosis-page)
* [Specialize Page](#specialize-page)
* [Available Appointments Page](#available-appointments-page)
* [Technologies Used](#technologies-used)
* [Done by](#done-by)
* [Superviser](#superviser)

## Run Localy

```python manage.py runserver``` then navigate to  [127.0.0.1:8000](https://localhost:8000).
## **Abstract:**
#### *Our project is a website for booking online to clinic and a doctor that will make it easy for the patient to navigate through different clinics that are in website.The website navegation bar contains Home, Registration, Login, and Contact Us.Doctors must approved from admin. After choose the clinic, the patient can see all doctors are in it with each free time for each doctor that mentioned by a doctor .The patients can add an appointment if they log in.They will also have the chance to knew their diagnosis ,and they also have the chance to cancel any appointment (AJAX working in this button).The doctors have to update diagnosis of patient in the patient diagnosis page to knew the status diagnosis of that patient. All the pages in our website aregoing to be responsive.*
## Main Page:
* Features:
     *  Mainpage have a navigation bar contains a route to (Home),(Registration), (Login), and (Contact Us).
     *  Users are able to see what clinics avilable in website, if they press on home on top of the navigation bar.
     *  Users are able to contact us, if they press on contact us on top of the navigation bar.
   ### Main Page Preview:
   ![main page](https://user-images.githubusercontent.com/110983334/195993187-72fa0bed-9816-4f13-a417-513948def833.gif)
## Home Page:
* Features:
     *  Display types of clinics in our website.
     *  Users are able to see what a doctors had a free time , if they press on book here button.
     *  Homepage have a navigation bar contains a route to (Registration), (Login), and (Contact Us). 
   ### Home Page Preview:
   ![home page](https://user-images.githubusercontent.com/110983334/195993292-b7c96adc-653d-4f0f-8e11-dc1777c80469.gif)
   
## Contact Us Page:
* Features:
     *  Display our contacts.
     * Contactuspage have a navigation bar contains a route to (Home) (Registration), and (Login).
   ### Contact Us Preview:
   ![Contact us page](https://user-images.githubusercontent.com/110983334/195993460-f564accc-a642-4d71-a7fe-af231d432a3e.png)
## Login and Registration:
* Features
    *	Users are able to register:
    *	Users will not be able to register with two different accounts with same email.
    *	Username must contain 2 characters at least.
    *	Password must contain at least 8 characters.
    *	Passwords are encrypted.
    *	Validations are done in real time
    *	User information are saved in session, so they don’t need to log in again.
    * User will be able to login.
    *	User is only able to login with a valid password and email.
    *	User should be saved in session when registered successfully.
  ### Login/Register Preview
  ![login](https://user-images.githubusercontent.com/110983334/195993499-90c39ad1-3192-4b61-8e21-335452cd0413.png)
  ![registration](https://user-images.githubusercontent.com/110983334/195993501-7afcc71d-af9a-4b0f-88a0-27e3e9511e13.png)
  
## Doctor Dashboard Page:
* Features
   * The doctor dashboard page can be viewed when a doctor login.
   * The doctor dashboard page include an appointments that doctor have. 
   * Edit button send to a page let doctor add which time free for him.
   * If doctor click on show send him to patient diagnosis page who's make an appointment.
   * After doctor finished the patient visit click on confirm visit send to update page to add his diagnosis to patient diagnosis page. 
   * Logout button redirect to main page.  
  ### Doctor Dashboard Preview
  ![doctor dashboard page](https://user-images.githubusercontent.com/110983334/195993556-39312676-6a28-4130-a731-8fa39b4cc1ce.png)
## Patient Dashboard Page:
* Features
   * The patient dashboard page can be viewed when a patient login.
   * The patient dashboard page include an appointments that patient have. 
   * If patient click on cancel button that mean he is cancel the appointment.
   * Add new appointment button send to home page if the patient need to book a new appointment.
   * If patient click on show button send him to patient diagnosis page to see his diagnosis.
   * Logout button redirect to main page.  
  ### Patient Dashboard Preview
  ![patient dashboard](https://user-images.githubusercontent.com/110983334/195993606-e35c26e5-1993-4368-b893-3e7ed90f14cc.png)
## CheckBox Page:
* Features
   * The checkbox page display days with time.
   * The doctor can book which day and time free for him.
   * When click on book sessions button add the choosen day and time to specialize page.
   * Back button redirect to doctor dashboard page. 
   * Logout button redirect to main page.  
  ### CheckBox Preview
  ![CheckBox page](https://user-images.githubusercontent.com/110983334/195993632-db471ac6-e60b-4943-879f-6ff0d8e27c94.png)
## Update Page:
* Features
   * The update page display a form to a doctor user.
   * The doctor can add his diagnosis after patient visit.
   * When click on update button the diagnosis added to patient diagnosis page.
   * Dashboard button redirect to doctor dashboard page. 
   * Logout button redirect to main page.  
  ### Update Preview
  ![update page](https://user-images.githubusercontent.com/110983334/195993653-35e719d7-0cfb-421c-86db-8cb59641169a.png)
## Patient Diagnosis Page:
* Features
   * The patient diagnosis page display all patient diagnostics if patient loged in.
   * If doctor loged in can add his diagnosis to the patient diagnostics by click on update button.
   * Dashboard button redirect to doctor/patient dashboard page. 
   * Logout button redirect to main page.  
  ### Patient Diagnosis Preview
  ![patient diagnosis page](https://user-images.githubusercontent.com/110983334/195993682-39744690-cc15-413f-a0ad-8f16e5fe15ba.png)
## Specialize Page:
* Features
   * The specialize page display all doctors available for book.
   * The select options contain locations of doctors.
   * When click on search button display all doctors available in choosen location.
   * Back to clinics button send to home page.
   * Book button send to available appointments page if patient loged in,if not send to login and registration page.
  ### Specialize Preview
  ![specialize page](https://user-images.githubusercontent.com/110983334/195993708-034bac6c-1402-44ad-9021-bce433c61d16.png)
## Available Appointments Page:
* Features
   * The available appointments page display all doctors free time.
   * Home button send to home page.
   * When click on back button send to specialize page.
   * Dashboard button send to patient dashboard page.
  ### Available Appointments Preview
  ![available appointments](https://user-images.githubusercontent.com/110983334/195993728-42494146-f733-4a9f-9ae6-9baeea0785b2.png)
  
## Technologies Used:
- python - version 3.10.7.
- Django - version 2.2.4.
- bootstrap - version 4.5.3.
- jQuery and AJAX.
  ![Technologies](https://user-images.githubusercontent.com/75543501/121818529-7417b600-cc90-11eb-97b0-59ebfe43f47c.png)
## Done by:
- Abdalfattah Hasanat. 
- Ra'd Abdallah.  
- Sura Qalalwa.
- Amin Hotari.
## Superviser:
- Amin Eid.
- Fatima Harahsheh.
