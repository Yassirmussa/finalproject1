# urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('login', views.login),
    path('register', views.register),
    
    path('', views.index, name='index'),
    
    path('stafflist/', views.stafflist, name='stafflist'),
    path('registerstaff/', views.registerStaff, name='staffregistration'),
    path('editstaff/<int:Sid>/', views.updateStaff, name='edit_staff'),
    
    path('workdays/', views.workdays, name='workdays'),
    
    path('getfeedback/', views.getFeedback, name='user-feedback'),
    
    path('getallocation', views.getAllocation, name='allocation')
]
