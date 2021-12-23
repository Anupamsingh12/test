from django.shortcuts import render,HttpResponse,redirect
import os
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import consignment

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    curr_user =request.user
    return render(request,"home.html",{'user':curr_user})

def adminApp(request):
    if not request.user.is_authenticated:
       
        return redirect('login')
    curr_user =request.user
    print(curr_user.first_name)
    return render(request,"home.html",{'user':curr_user})

def status2(request):
    return render(request,'status2.html')
   
def contact(request):
    return render(request,'contact.html')

def track(request):
     current_user = request.user
     cons=""
     if request.method=="POST":

         eml=request.POST["email"]   
         
         cons=consignment.objects.filter(email=eml) 
         if not cons:
             messages.info(request,'nothing is found') 
         
         
     
     return render(request,'track.html',{'user':current_user,"cons":cons})



def login(request):
    if request.method=="POST":
        username1=request.POST['username']
        password=request.POST["password"]
        username=""
        if "@" in username1:
            username2=username1.split("@")
            username=username2[0]
        else:
            username=username1


        user=auth.authenticate(username=username,password=password)
    
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
        else:
            messages.info(request,'username or password is not correct')
        return render(request,'login.html')

        


    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        #print(request.POST.keys())
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        email=request.POST['email']
        password1=request.POST['Password1']
        password2=request.POST['Password2']
        
        nm=email.split('@')
        username=nm[0]
        if password1 !=password2:
            messages.info(request,'password not matched')

        else:
            password=password1
            user=User.objects.create_user(username=username,password=password,email=email,first_name=firstName,last_name=lastName)
            user.save()
            print("user_created")
            return render(request,'login.html')
        
        
    return render(request,'signup.html')




def send(request):
    if request.method=="POST":
        print(request.POST.keys())
       
        email=request.POST['email']
        name=request.POST['name']
        itemWeight=request.POST['itemWeight']
        contact=request.POST["contact"]
        pincode=request.POST["pincode"]
        address=request.POST['address']
        itemWeight=float(itemWeight)
        con=consignment(name=name,email=email,dest=address,pincode=pincode,item_weight=itemWeight,contact=contact,status="packed")
        con.save()
       

        messages.info(request,'submitted sucessfully')
        return redirect('sendparcel.html')

         

    return render(request,"sendparcel.html")


def status(request):
    current_user = request.user 
    return render(request,'status.html')
    #ed=raised_issue.objects.filter(email=current_user.email)


def logout(request):
    auth.logout(request)
    return render(request,"home.html")

def suggesions(request):
    return render(request,'home.html')





