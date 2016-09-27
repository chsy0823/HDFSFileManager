from django.shortcuts import render
from .models import InstanceItem

def getList(request):
    instance = InstanceItem()
    #user.insert("temp","1234","yong",1,"01098569155")
    #lst = instance.getInstanceItems("/tmp/crawler/cars")
    return render(request, 'imageviewer/list.html', {'list':None})

# Create your views here.
