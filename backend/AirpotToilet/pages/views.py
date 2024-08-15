from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirmpass = request.POST['confirm_password']
        
        if password == confirmpass:
            user = User.objects.create_user(username=username,email=email, password=password)
            user.save()
            messages.info(request, 'User registred succesiffully')
        else:
            messages.info(request, 'Password not match')
        return render(request, 'registerUser.html')
    return render(request, 'registerUser.html')

def index(request):
    return render(request, 'index.html')

def stafflist(request):
    return render(request, 'stafflist.html')

def registerStaff(request):
    return render(request, 'registerStaff.html')

def updateStaff(request, Sid):
    return render(request, 'updatestaff.html')

def workdays(request):
    return render(request, 'workdays.html')



def getFeedback(request):
    return render(request, 'getFeedback.html')

def getAllocation(request):
    return render(request, 'getAllocation.html')
