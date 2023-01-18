from django.shortcuts import render,redirect,HttpResponse
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if not(name == '' or email == '' or phone == '' or desc == ''):
            contact = Contact(name = name,email = email,phone = phone,desc = desc)
            contact.save()
            messages.success(request,'Your form has been submitted!')

        else:
            messages.warning(request,'Please fill all the entries below!')
            

    return render(request,'contact.html')



def flavour(request):
    return render(request,'flavour.html')


def signupUser(request):
    signupUsername = request.POST.get('username')       
    signupPassword = request.POST.get('password1')       
    signupConfirmPassword = request.POST.get('password2')

    if request.method == 'POST' and not(signupUsername == '' or signupPassword == '' or signupConfirmPassword ==''):
        if signupPassword == signupConfirmPassword:
            new_user = User.objects.create_user(username=signupUsername,password=signupPassword)
            new_user.save()
            messages.success(request,'Your account has been created successfully!')            

            return redirect('/signin')
          
    return render(request,'signup.html')


def loginUser(request):
    if request.method == "POST":
        loginUsername = request.POST.get("username")            
        loginPassword = request.POST.get("password")  

        user_auth = authenticate(request,username = loginUsername,password = loginPassword) 

        if user_auth is not None:
            login(request,user=user_auth)
            messages.success(request,'Successfully loged in!')
            return redirect('/')

        else:
            return redirect('/signin')
                

    return render(request,'signin.html')