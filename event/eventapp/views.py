from django.shortcuts import render,redirect
from .forms import Familyforms
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import Buisness,Charity,Family,Bookevent,Contactus,Culture
from django.contrib.auth.decorators import login_required  

def buisness(request):
    buisness=Buisness.objects.all()
    return render(request,"buisness.html",{"buisness":buisness})
def family(request):
    family=Family.objects.all()
    return render(request,"family.html",{"family":family})

def charity(request):
    charity=Charity.objects.all()
    return render(request,"charity.html",{"charity":charity})

def culture(request):
    culture=Culture.objects.all()
    return render(request,"culture.html",{"culture":culture}) 

@login_required(login_url='login')
def user_cart(request):
    user_cart=Bookevent.objects.filter(user=request.user)
    return render(request,"user_cart.html",{"user_cart":user_cart})


def contact(request):
    return render(request,'contact.html')

@login_required(login_url='login')
def bookevent(request):
    if request.method=="POST":
        Name=request.POST['name']
        Mobile=request.POST['mobile']
        Location=request.POST['location']
        Email=request.POST['email']
        People=request.POST['people']
        Date=request.POST['date']
        Event=request.POST['event']
        Food=request.POST['food']
        Address=request.POST['address']
        Message=request.POST['message']
        if ((Mobile and Email and Address)==''):
            messages.info(request,'warning fields must be taken')
            return redirect('bookevent')
        else:
            guest=Bookevent(Name=Name,Mobile=Mobile,Location=Location,Email=Email,People=People,Date=Date,Event=Event,Food=Food,Address=Address,Message=Message)
            guest.user=request.user
            guest.name=request.user
            guest.save()
            messages.info(request,'your event has been booked')
            return redirect('/')
    return render(request,'bookevent.html')
    
def base(request):
    if request.method=='POST':
        Name=request.POST.get('Name')
        Mobile=request.POST.get('Mobile')
        Email=request.POST.get('Email')
        Message=request.POST.get('Message')
        if((Name and Mobile and Email and Message)==""):
            messages.info(request,"invalid msg form")
            return redirect('home')
        else:
            Contact_msg=Contactus(Name=Name,Mobile=Mobile,Email=Email,Message=Message)
            Contact_msg.save()
            messages.info(request,"Messages has been sent")
            return redirect('home')
    else:
        return render(request,'base.html')
    

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
           auth.login(request,user)
           user.save()
           return redirect('/')
        else:
            messages.info(request,'password did not match')
            return redirect('/')
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Register Know')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,'account hasbeen created')                
                return redirect("login") 
        else:
            messages.info(request,'password didnot match')
            return redirect('register')
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render(request,'about.html')
