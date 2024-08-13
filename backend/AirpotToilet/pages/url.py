# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stafflist/ ', views.stafflist, name='stafflist'),
    path('workdays/', views.workdays, name='workdays'),
    path('registerstaff/', views.registerStaff, name='staffregistration')
]
