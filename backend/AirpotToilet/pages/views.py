from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def stafflist(request):
    return render(request, 'stafflist.html')

def workdays(request):
    return render(request, 'workdays.html')

def registerStaff(request):
    return render(request, 'registerStaff.html')
