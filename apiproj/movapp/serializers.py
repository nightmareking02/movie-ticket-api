from rest_framework import serializers
from movapp.models import Movies

class movieserializers (serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields=['title','cast','type','budget','collection','streaming','rating']