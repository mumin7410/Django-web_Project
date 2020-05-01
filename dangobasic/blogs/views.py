from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import post, card
# Create your views here.
def hello (request):
    return render(request, 'page1.html')
    
def page1 (request):
    return render(request, 'page1.html')

def created1(request):
    return render(request, 'createdform.html')

def addblog(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username = username).exists():
            messages.info(request,'username is already used')
            return redirect('/createdform')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'email is already used')
            return redirect('/createdform')
        else:
            user = User.objects.create_user(
            username = username,
            first_name = firstname,
            last_name = lastname,
            email = email,
            password = password
            )
            user.save()      
        return render(request, 'result.html' )
    else:
        messages.info(request, 'Password is not same')
        return redirect('/createdform')

def loginform(request):
    return render(request, 'login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username = username, password = password)

    if user is not None:
        auth.login(request, user)
        return redirect('/page1')
    else:
        messages.info(request,'username is not in system')
        return redirect('/loginform')

def logout(request):
    auth.logout(request)
    return redirect('/page1')

def resulting(request):
    data = post.objects.all()
    data_1 = card.objects.all() 
    return render(request, 'result.html',{'cards':data_1} )






