from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect("/")
#         else:
#             messages.info(request, 'Invalid credentials')
#             return redirect('login')
#     else:
#         return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Replace 'username' with 'email'
        password = request.POST.get('password')
        
        # Authenticate using the email and password
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")  # Redirect to the home page or another page
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# def register(request):
#     if request.method =='POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         password = request.POST['password']
#         confirmpass = request.POST['confirm_password']
        
#         if password == confirmpass:
#             user = User.objects.create_user(username=username,email=email, password=password)
#             user.save()
#             messages.info(request, 'User registred succesiffully')
#         else:
#             messages.info(request, 'Password not match')
#         return render(request, 'registerUser.html')
#     return render(request, 'registerUser.html')
from .models import User

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirm_password')
        
        if password == confirmpass:
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(email=email, password=password, phone=phone)
                user.save()
                messages.info(request, 'User registered successfully')
            else:
                messages.info(request, 'Email is already registered')
        else:
            messages.info(request, 'Passwords do not match')
        return render(request, 'registerUser.html')
    
    return render(request, 'registerUser.html')



@login_required()
def index(request):
    return render(request, 'index.html')

@login_required()
def stafflist(request):
    return render(request, 'stafflist.html')

@login_required()
def registerStaff(request):
    return render(request, 'registerStaff.html')

@login_required()
def updateStaff(request, Sid):
    return render(request, 'updatestaff.html')

@login_required()
def workdays(request):
    return render(request, 'workdays.html')

@login_required()
def getFeedback(request):
    return render(request, 'getFeedback.html')

@login_required()
def getAllocation(request):
    return render(request, 'getAllocation.html')

@login_required()
def updateAllocation(request, Aid):
    return render(request, 'updateAllocation.html')
