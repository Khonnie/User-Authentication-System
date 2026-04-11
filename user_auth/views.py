from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'user_auth/index.html')

def signin(request):
    if request.method == 'POST':
        #Collecting/taking the username and password from the user and storing them into variables
        username = request.POST['username']
        password = request.POST['password']
        #Autheticating the user to check if the username and password are the ones in the system
        user = authenticate(request, username=username, password=password)

        if user is not None: #if user credentials are correct,and the credentials match/are correct login user
            login(request, user)
            first_name = user.first_name
            return render(request, 'user_auth/index.html', {'first_name': first_name})

        else:
            messages.error(request, 'Bad Credentials')
            return redirect(request, 'app_name:home')



    return render(request, 'user_auth/signin.html')

def signup(request):
    if request.method == 'POST':
       # username = request.POST.get('username')
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
       # after the user submitting their data/collecting user data, we shall register the user in the database and save the user data in the database
       # we will make use of a django inbuilt user model to register the user in the database and save the user data in the database
        #to do that we first import the user model from django.contrib.auth.models import User
        # then we will create a user object and save the user data in the database using the create_user method of the user model
        my_user = User.objects.create_user(username, email, password) 
        my_user.first_name = first_name
        my_user.last_name = last_name

        my_user.save() # this will save the user data in the database
        #if the user is regidtered successfully, we will show him a message that he is registered successfully and then we will redirect him to the signin page
        #for thus we are making use of messages from django by using from django.contrib import messages
        messages.success(request, 'Your account has been successfully created.')
        #as soon as the user is registered successfully, we will redirect him to the signin page
        return redirect('user_auth:signin')
        
        # we will also check if the username is already taken before registering the user
        
       # we will also check if the password and confirm password are the same before registering the user

    return render(request, 'user_auth/signup.html')

def profile(request):
    return render(request, 'user_auth/profile.html')

def signout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('user_auth:home')
