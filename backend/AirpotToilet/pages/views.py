from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

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
