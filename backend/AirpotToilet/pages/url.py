# urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='registration'),
    
    path('', views.index, name='index'),
    
    path('stafflist/', views.stafflist, name='stafflist'),
    path('registerstaff/', views.registerStaff, name='staffregistration'),
    path('editstaff/<int:Sid>/', views.updateStaff, name='edit_staff'),
    
    path('workdays/', views.workdays, name='workdays'),
    
    path('getfeedback/', views.getFeedback, name='user-feedback'),
    
    path('allocate/', views.allocate, name='allocate'),
    
    path('getallocation', views.getAllocation, name='allocation'),
    path('updateallocation/<int:Aid>/', views.updateAllocation, name='edit_allocation'),
]
