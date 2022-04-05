from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
# from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings
# Create your views here.

def index(request):
    plans=Plan.objects.all()
    data={'plans':plans}
    return render(request,'index.html',data)


def About(request):
    return render(request,'About.html')


def Services(request):
    return render(request,'Services.html')   


def tutorial(request):
    return render(request,'tutorial.html')     


# def Contact(request):
#     return render(request,'Contact.html')


def add_contact(request):
    error=""
    if request.method=="POST":
        n=request.POST['name']
        l=request.POST['last_name']  
        c=request.POST['contact']
        e=request.POST['email']
        a=request.POST['age']
        d=request.POST['describe']


        try:
            Contact.objects.create(First_Name=n,Last_Name=l,Contact=c,Email_Id=e,Age=a,Describe=d)
            error ="no"

        except:
            error="yes"


    d={'error':error}
    return render(request,'Contact.html',d)     


def view_contact(request):
    if not request.user.is_staff:
        return('admin_login')

    cont=Contact.objects.all()
    data={'cont':cont}
    return render(request,'view_contact.html',data)


def delete_contact(request):
    pid=request.GET['pid']
    con=Contact.objects.get(id=pid)
    con.delete()
    return redirect('view_contact')



def admin_homepage(request):
    if not request.user.is_staff:
        return redirect('admin_login')

    
    eqp=Equipments.objects.all()
    plan=Plan.objects.all()
    mem=Contact.objects.all()
    
    b1=0
    c1=0
    d1=0


    for i in eqp:
        b1+=1

    for i in plan:
        c1+=1
    for i in mem:
        d1+=1
    d={'b1':b1,'c1':c1,'d1':d1}
    res=render(request,'admin_homepage.html',d)
    return res


def admin_login(request):
    data={}
    if request.method=="POST":
        u=request.POST['admin']
        p=request.POST['pwd']

        user=authenticate(request,username=u,password=p)
        if user:
            login(request,user)
            return redirect('admin_homepage/')

        else:
            data['error']="Login Failed..Either Username or password is incorrect"
            return render(request,'login.html',data)

    else:
        return render(request,'login.html',data)   


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


def add_plan(request):
    error=""
    if not request.user.is_staff:
        return('admin_login')

    if request.method=="POST":
        n=request.POST['Name']
        a=request.POST['Amount']
        d=request.POST['Duration']

        try:
            Plan.objects.create(Name=n,Amount=a,Duration=d)
            error="no"

        except:
            error="yes"

    data={'error':error}
    return render(request,'add_plan.html',data)



def view_plan(request):
    if not request.user.is_staff:
        return('admin_login')
    pla=Plan.objects.all()
    data={'pla':pla}
    return render(request,'view_plan.html',data)


def delete_plan(request):
    pid=request.GET['pid']
    enq=Plan.objects.get(id=pid)
    enq.delete()
    return redirect('view_plan') 


def add_equipments(request):
    error=""
    if not request.user.is_staff:
        return('admin_login')

    if request.method=="POST":
        n=request.POST['Name']
        p=request.POST['Price']
        u=request.POST['Unit']
        d=request.POST['Date']
        de=request.POST['Description']

        try:
            Equipments.objects.create(Name=n,Price=p,Unit=u,Date=d,Description=de)
            error="no"

        except:
            error="yes"
    data={'error':error}
    return render(request,'add_equipments.html',data)




def view_equipments(request):
    if not request.user.is_staff:
        return('admin_login')

    equip=Equipments.objects.all()
    data={'equip':equip}
    return render(request,'view_equipments.html',data)



def delete_equipments(request):
    pid=request.GET['pid']
    enq=Equipments.objects.get(id=pid)
    enq.delete()
    return redirect('view_equipments')


def add_member(request):
    error=""
    if not request.user.is_staff:
        return('admin_login')
    if request.method=="POST":
        n=request.POST['name']
        l=request.POST['last_name']  
        c=request.POST['contact']
        e=request.POST['email']
        a=request.POST['age']


        try:
            Member.objects.create(First_Name=n,Last_Name=l,Contact=c,Email_Id=e,Age=a)
            error ="no"

            # subject = 'Internship Python'
            # message = 'dear Candidate,\nWe are pleased to inform that you are selected our 6 months free inernship program..'
            # recipient = Member.cleaned_data.get('Email_Id')
            # send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            # messages.success(request, 'Success!')
            # return redirect('/')

        except:
            error="yes"


    d={'error':error}
    return render(request,'add_member.html',d)     


def view_member(request):
    if not request.user.is_staff:
        return('admin_login')

    mem=Member.objects.all()
    data={'mem':mem}
    return render(request,'view_member.html',data)


def delete_member(request):
    pid=request.GET['pid']
    mem=Member.objects.get(id=pid)
    mem.delete()
    return redirect('view_member')    