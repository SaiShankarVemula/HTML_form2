from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('<h1>Topic_name is Inserted</h1>')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    LWO=Topic.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        return HttpResponse('<h1>Webpage is Inserted</h1>')

    return render(request,'insert_webpage.html',context=d)

def insert_accessrecord(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}

    if request.method=='POST':
        na=request.POST['na']
        dt=request.POST['dt']
        au=request.POST['au']

        WO=Webpage.objects.get(name=na)
        AO=Accessrecord.objects.get_or_create(name=WO,date=dt,author=au)[0]
        AO.save()
        return HttpResponse('<h1>Accessrecord is Inserted</h1>')
    
    return render(request,'insert_accessrecord.html',d)


def retrieve_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        print(MSTS)
        RWOS=Webpage.objects.none()

        for i in  MSTS:
            RWOS=RWOS|Webpage.objects.filter(topic_name=i)

        d1={'RWOS':RWOS}
        return render(request,'display_webpages.html',d1)


    return render(request,'retrieve_webpage.html',d)



def Checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    
    return render(request,'Checkbox.html',d)
