from app1.models import Company_Data
from django.shortcuts import render

# Create your views here.

def Company_login(request):
    if request.POST:
        em = request.POST['email']
        ps = request.POST['pass']
        print (em, ps)
    return render(request,'company/login/login.html')

def Company_regi(request):
    if request.POST:
        nm = request.POST['name']
        em = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']

        if  pass1 == pass2:
           obj = Company_Data()
           obj.com_name = nm
           obj.com_em = em
           obj.com_pass = pass2
           obj.save()
        else :
           print("Wrong Password...")




    return render(request,'company/login/regi.html')

