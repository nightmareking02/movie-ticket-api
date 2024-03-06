from django.shortcuts import render
from apiapp.models import Trains
from apiapp.serializers import TrainsSerializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.


@csrf_exempt
def trainapi(request,id=0):
    if request.method =="GET":
        trains= Trains.objects.all()
        trains_seralizers=TrainsSerializers(trains,many=True)
        trainsdata1=trains_seralizers.data
        return JsonResponse(trainsdata1,safe=False)
    elif request.method =="POST":
        val=JSONParser().parse(request)
        val1=TrainsSerializers(data=val)
        if val1.is_valid():
            val1.save()
            return JsonResponse("data is added",safe=False)
        return JsonResponse("not added")
    elif request.method=="PUT":
        trainsid=JSONParser().parse(request)
        trainsdata=Trains.objects.get(id=trainsid['id'])
        trains_serial=TrainsSerializers(trainsdata,data=trainsid)
        if trains_serial.is_valid():
            trains_serial.save()
            return JsonResponse("data added",safe=False)
        return JsonResponse("data not added",safe=False)
    
    # elif request.method=="DELETE":
    #     trainsid=JSONParser().parse(request)
    #     trainsdata=Trains.objects.get(id=trainsid['id'])
    #     if trainsdata == True:
    #         trainsdata.delete()
    #         return JsonResponse("data is deleted",safe=False)
    #     return JsonResponse("INVALID DATA",safe=False)

    elif request.method =="DELETE":
        trains=Trains.objects.get(id=id)
        trains.delete()
        return JsonResponse("DATA IS DELETED",safe=False)

def index(request):
    return render(request,"index.html",{})

@csrf_exempt
def savefile(request):
    filedata=request.FILES['file']
    filesname=default_storage.save(filedata.name,filedata)
    return JsonResponse(filesname,safe=False)

class createmodel(CreateView):
    model=Trains
    fields=['id','name','train_no','start','end','price','timing','type']
    success_url=reverse_lazy('/')
