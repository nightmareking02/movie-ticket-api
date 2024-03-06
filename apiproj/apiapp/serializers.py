from rest_framework import serializers
from apiapp.models import Trains

class TrainsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Trains
        fields=['id','name','train_no','start','end','price','timing','type']