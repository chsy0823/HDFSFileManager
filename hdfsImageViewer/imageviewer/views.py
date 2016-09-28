from django.shortcuts import render
from .models import InstanceItem

def getInstanceList(request):

    instance = InstanceItem()
    lst = instance.getInstanceList_model("/tmp/crawler")

    return render(request, 'imageviewer/instance_list.html', {'list':lst})

def getInstanceItems(request):

    instance = InstanceItem()

    categoryName = request.POST['crawl_name']

    #user.insert("temp","1234","yong",1,"01098569155")
    lst = instance.getInstanceItems_model("/tmp/crawler/"+categoryName)

    return render(request, 'imageviewer/instanceItem_list.html', {'category_name':categoryName, 'list':lst, 'list_size':len(lst)})

def removeInstance(request):

    instance = InstanceItem()

    checkList = request.POST.getlist('deleteChk')
    categoryName = request.POST['crawl_name']

    for path in checkList :
        instance.removeFileFromPath(path)
    
    return render(request, 'imageviewer/remove_list.html', {})

# Create your views here.
