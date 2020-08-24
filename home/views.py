from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from team.models import *

def homePage(request):
    content={
        'items':Item.objects.all().first(),
        'slides':Slide.objects.all(),
        'sponsors':Sponsor.objects.all(),
        'contacts':Contact.objects.all().first()
    }
    return render(request, 'home/home.html',content)
def carDetail(request, pk):
    team=Team.objects.get(year=pk)
    car=Car.objects.get(team=team)
    members=TeamMember.objects.filter(team=team).order_by('name')
    content={
        'items':Item.objects.all().first(),
        'car':car,
        'details':CarDetail.objects.filter(car=car),
        'members':members
    }
    return render(request,'home/car.html',content)
@api_view(['GET'])
def saveMsg(request):
    msg = Message.objects.all()
    serializer = MessageSerializer(msg, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def svMsg(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def showSlide(request):
    slide = Slide.objects.all()
    serializer = SlideSerializer(slide, many=True)
    return Response(serializer.data)

def carsPage(request):
    content={
        'cars':Car.objects.all(),
        'contacts':Contact.objects.all().first(),
        'items':Item.objects.only('logo').first()}
    return render(request,'home/cars.html',content)

def teamPage(request):
    layr=Team.objects.last()
    content={
        'members':TeamMember.objects.filter(team=layr),
        'contacts':Contact.objects.all().first(),
        'systems':Subsystem.objects.all(),
        'team':Team.objects.all().last(),
        'items':Item.objects.only('logo').first()
    }
    return render(request,'home/team.html',content)