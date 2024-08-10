from . import views
from django.urls import path

urlpatterns = [
    # STAFF API's
    path('insertstaff', views.createStaff),
    path('getstaff', views.getStaff),
    path('updatestaff/<Sid>/', views.updateStaff),
    path('deletestaff/<Sid>/', views.deleteStaff),

    # FEEDBACK API's
    path('insertfeedback', views.createFeedback),
    path('getfeedback', views.getFeedback),
    path('updatefeedback/<Fid>/', views.updateFeedback),
    path('deletefeedback/<Fid>/', views.deleteFeedback),


    # DAY API's
    path('insertday', views.createDay),
    path('getday', views.getDay),
    path('getdaybyid/<int:Did>/', views.getDayByID),
    path('updateday/<int:Did>/', views.updateDay),
    path('deleteday/<int:Did>/', views.deleteDay),

    #  ALLOCATION API's
    path('insertallocation', views.createAllocation),
    path('getallocation', views.getAllocation),
    path('getallocationbyid/<int:Aid>/', views.getAllocationByID),
    path('updateallocation/<int:Aid>/', views.updateAllocation),
    path('deleteallocation/<int:Aid>/', views.deleteAllocation),

]