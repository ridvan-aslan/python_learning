from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print('Username already exists')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                print('Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print('User created')
                return redirect('login')
        else:
            print('Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    return render(request, 'user/logout.html')