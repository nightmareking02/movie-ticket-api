from django.db import models

# Create your models here.

class Trains(models.Model):
    name= models.CharField(max_length=50)
    train_no= models.IntegerField()
    start= models.CharField(max_length=50)
    end=models.CharField(max_length=50)
    price= models.IntegerField()
    timing= models.TimeField(default=False,auto_now_add=False)
    type= models.CharField(max_length=50)