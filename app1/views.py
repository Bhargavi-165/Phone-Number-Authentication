from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import * 
import random

import random
import smtplib
from email.message import EmailMessage

def layout(request):
    return render(request,"layout.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request,"login.html")

otp_list = []

def logincheck(request):
    if request.method=="POST":
        try:
            r=Register.objects.get(phone=request.POST.get('phone'),email=request.POST.get('email'),password=request.POST.get('password'))
            print(r.fullname)
            otp_list.clear()
            otp = random.randint(10000,99999)
            print(otp)
            otp_list.append(otp)
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('bashamasthan31@gmail.com','dygq eorh yspf jhbx')
            msg = EmailMessage()
            msg['From'] = 'Aunthentication Domain'
            msg['Subject'] = 'OTP Verification'
            msg.set_content(f"Your One Time Password is: {otp} \n Thank you for Choosing Our Platform to Improve Your Knowledge")
            msg['To'] = r.email
            server.send_message(msg)
            return redirect('/otp')
            return HttpResponse("Login Success")

        except Exception as ex:
            return render(request,"login.html",{"msg":"Invalid Email/Password"})
   
    return render(request,"login.html",{"msg":"Invalid Designation"})


def uotp(request):
   
    return render(request, "auth.html")

def otp_check(request):
    if request.method == "POST":
        uotp=request.POST.get('otp')
        otp = otp_list[0]
        if int(uotp) == int(otp):
            return redirect('/userhome')
    return render(request,'auth.html',{"msg":"Invalid OTP!"})



def about(request):
    return render(request,"about.html")

def register(request):
    return render(request,"register.html")

def doregister(request):
    fullname=request.GET['fullname']
    email=request.GET['email']
    password=request.GET['password']
    phone=request.GET['phone']
    r=Register()
    r.fullname=fullname
    r.email=email
    r.password=password
    r.phone=phone
    r.save()
    return render(request,"login.html",{"msg":"Registration Successful"})

def index(request):
    return render(request,"layout.html")

def viewusers(request):
    users=Register.objects.all()
    return render(request,"viewusers.html",{"users":users})

def userhome(request):
    return render(request,"userhome.html")

def adminhome(request):
    return render(request,"adminhome.html")

def modify(request):
    operation=request.GET['operation']
    fullname=request.GET['fullname']
    email=request.GET['email']
    password=request.GET['password']
    desig=request.GET['desig']
    r=Register.objects.get(email=email)
    r.fullname=fullname
    r.email=email
    r.password=password
    r.desig=desig
    if operation=="update":
        r.save()
    else:
        Register.delete(r)
    users=Register.objects.all()
    return render(request,"viewusers.html",{"users":users})

def msg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        m=Contact_data(fullname=name,phone=phone,email=email,msg=msg)
        m.save()
        return redirect('/login/')
    return render(request,'contact.html',{'msg':"Email already Exists!",})