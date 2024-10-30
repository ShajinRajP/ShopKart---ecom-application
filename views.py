from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request, "Password is not matching  ")
            return render(request, 'authentication/signup.html')
            #return redirect('/auth/signup')
        
        try:
            if User.objects.get(username=email):
                messages.info(request, "Email already exist")
                return render('authentication/signup')
            return render('authentication/signup')
        
        except Exception as identifier:
            pass
        
        user = User.objects.create_user(email,email,password)
        user.save()
        messages.success(request, "User created successfully")
        return render(request, "authentication/login.html")  
    return render(request, "authentication/signup.html")


def handlelogin(request):
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username, password=userpassword)
        
        if myuser is not None:
            login(request, myuser)
            #messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/auth/login')
    
    return render(request, "authentication/login.html")




def handlelogout(request):
    logout(request)
    return redirect('/')


