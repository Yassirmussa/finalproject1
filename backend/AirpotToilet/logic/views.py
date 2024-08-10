from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Staff,Day,Allocation,Feedback
from .serializers import StaffSerializer,DaySerializer,AllocationSerializer,FeedbackSerializer
# Create your views here.

# STAFF
@api_view(['POST'])
def createStaff(request):
    serializer = StaffSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getStaff(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data, status=200)

@api_view(['PUT'])
def updateStaff(request, Sid):
    try:
        staff = Staff.objects.get(Sid = Sid)
        serializer = StaffSerializer(staff, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except:
        return Response(f' staff {Sid} does not exist')

@api_view(['DELETE'])
def deleteStaff(request, Sid):
    try:
        staff = Staff.objects.get(Sid = Sid)
        staff.delete()
        return Response("Deleted Sucessifully", status=200)
    except:
        return Response(f' staff {Sid} does not exist')
    

#  FEEDBACK
@api_view(['POST'])
def createFeedback(request):
    serializer = FeedbackSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getFeedback(request):
    feedback = Feedback.objects.all()
    serializer = FeedbackSerializer(feedback, many=True)
    return Response(serializer.data, status=200)

@api_view(['PUT'])
def updateFeedback(request, Fid):
    try:
        feedback = Feedback.objects.get(Fid = Fid)
        serializer = FeedbackSerializer(feedback, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except:
        return Response(f' staff {Fid} does not exist')

@api_view(['DELETE'])
def deleteFeedback(request, Fid):
    try:
        staff = Staff.objects.get(Fid = Fid)
        staff.delete()
        return Response("Deleted Sucessifully", status=200)
    except:
        return Response(f' Feedback {Fid} does not exist')



# DAY

@api_view(['POST'])
def createDay(request):
    serializer = DaySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getDay(request):
    day = Day.objects.all()
    serializer = DaySerializer(day, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def getDayByID(request, Did):
    try:
        day = Day.objects.get(Did = Did)
        serializer = DaySerializer(day)
        return Response(serializer.data)
    except:
        return Response(f"Day with ID {Did} does not exist")

@api_view(['PUT'])
def updateDay(request, Did):
    try:
        day = Day.objects.get(Did = Did)
        serialzer = DaySerializer(day, data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=200)
        return Response(serialzer.errors)
    except:
        return Response(f"Day with ID {Did} does not exist")

@api_view(['DELETE'])
def deleteDay(request, Did):
    try:
        day = Day.objects.get(Did = Did)
        day.delete()
        return Response(f"Day with ID {Did} deleted successifully")
    except:
        return Response(f"Day with ID {Did} does not exist")


# ALLOCATION

@api_view(['POST'])
def createAllocation(request):
    serializer = AllocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getAllocation(request):
    allocation = Allocation.objects.all()
    serializer = AllocationSerializer(allocation, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def getAllocationByID(request, Aid):
    allocation = Allocation.objects.get(Aid = Aid)
    serializer = AllocationSerializer(allocation)
    return Response(serializer.data)
    

@api_view(['PUT'])
def updateAllocation(request, Aid):
    try:
        allocation = Allocation.objects.get( Aid = Aid)
        serializer = AllocationSerializer(allocation, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    except:
        return Response(f'Allocation with ID {Aid} does not exist')


@api_view(['DELETE'])
def deleteAllocation(request, Aid):
    try:
        allocation = Allocation.objects.get(Aid = Aid)
        allocation.delete()
        return Response(f'Allocation with ID {Aid} deleted successifully')
    except:
        return Response(f'Allocation with ID {Aid} does not exist')
