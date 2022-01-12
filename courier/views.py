from django.shortcuts import render,HttpResponse,redirect
import os
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import consignment,Profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    curr_user =request.user
    return render(request,"home.html",{'user':curr_user})

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile1 = Profile.objects.filter(user=request.user)
    profile=''
    for p in profile1:
        profile=p
    return render(request,"profile.html",{'profile':profile})

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
        return render(request,'profile.html')

        


    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        #print(request.POST.keys())
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        email=request.POST['email']
        password1=request.POST['Password1']
        password2=request.POST['Password2']
        
        gender=request.POST['gender']
        
        role=request.POST['role']
        user1=User.objects.filter(email=email)
        if user1 is None:
             messages.info(request,'user already exists')
             return render(request,'signup.html',{'message':messages})

        nm=email.split('@')
        username=nm[0]
        if password1 !=password2:
            messages.info(request,'password not matched')

        else:
            password=password1
            user=User.objects.create_user(username=username,password=password,email=email,first_name=firstName,last_name=lastName)
            user.save()
            profile =Profile(user=user)
            profile.save()
            profile = Profile.objects.get(user=user)
            profile.role = role
            profile.gender=gender
            profile.save()
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
    return render(request,'payment.html')
    

def logout(request):
    auth.logout(request)
    return render(request,"login.html")

def suggesions(request):
    return render(request,'home.html')

def updateProfile(request):
    print("entering updateProfile method")
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method=="POST": 
        if 'img' in request.FILES:
            img=request.FILES['img']
            if not img=='':
                print("yaha aaya")
                profile.userImage=img
                print("image set")
            
        firstName = request.POST['firstName']
        print(firstName)
        if not firstName=='':
            user.first_name=firstName
        lastName = request.POST['lastName']
        if not lastName=='':
            user.last_name=lastName
        contactNumber = request.POST['contactNumber']
        if not contactNumber=='':
            profile.contactNumber=contactNumber
        fatherName = request.POST['fatherName']
        if not fatherName=='':
            profile.fatherName=fatherName
        currentAddress = request.POST['currentAddress']
        if not contactNumber=='':
            profile.contactNumber=contactNumber
        permanentAddress = request.POST['permanentAddress']
        if not permanentAddress=='':
            profile.permanentAddress=permanentAddress
        email = request.POST['email']
        if not email=='':
            user.email=email
        birthday = request.POST['birthday']
        if not birthday=='':
            profile.birthDate=birthday
        user.save()
        profile.save()
        print("exiting update profile method")
    return render(request,'updateProfile.html',{'profile':profile})

def getUsers(request):
    pageNumber = 1
   # rr= request.GET['id']
    if request.GET =={}:
        pageNumber = 1
    else:
        pageNumber=request.GET['pageNumber']
    
    profile=Profile.objects.all().order_by('id')
    size = profile.count()
    paginator = Paginator(profile,10)
    totalPages =size//10 +1
    pageNumber = int( pageNumber)
    if size < (pageNumber-1) *10:
        return HttpResponse("<h1 style='text-align:center'> bad request 400</h1>")
    startIndex = (pageNumber-1)*10 +1
    viewSize =startIndex +10
    if size%10 < 10:
        viewSize= size % 10
    try:
        users=paginator.page(pageNumber)
    except PageNotAnInteger:
        users=paginator.page(1)
    except EmptyPage:
        users = paginator.page(1)
    rangeData=0
    if pageNumber ==4:
        rangeData=range()
    return render(request,'payment.html',{'profile':users,'totalPages':totalPages,'pageNumber':pageNumber,
    'resultSize':size,'startIndex':startIndex,'viewSize':viewSize,'range':range(1,4)})





