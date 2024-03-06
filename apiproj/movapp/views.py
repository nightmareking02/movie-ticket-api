from django.shortcuts import render
from movapp.models import Movies
from movapp.serializers import movieserializers
from django.http import JsonResponse

# Create your views here.


def movapi(request):
    if request.method=="GET":
        movies=Movies.objects.all()
        movies_serializers=movieserializers(movies,many=True)
        moviesdata=movies_serializers.data
        return JsonResponse(moviesdata,safe=False)