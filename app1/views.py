
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        
#  cheak your type password and conform pasword is same or note if both are same then login otherwise try again
       
        if pass1!=pass2:
            return HttpResponse("Your password and confermed pasword is NOT same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()

        # return HttpResponse("user has been created sucessfully!!!")
            return redirect('home')
        # print(uname,email,pass1,pass2) this is use for only test purpuse



    return render (request,'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')  # Fixed variable name for clarity
        user = authenticate(request, username=username, password=password)  # Authenticate user
        
        if user is not None:  # Check if authentication is successful
            login(request, user)  # Log in the user
            return redirect('/static/html/contact.html')  # Redirect to a named URL pattern or view
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')