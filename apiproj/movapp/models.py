from django.db import models

# Create your models here.

class Movies(models.Model):
    title= models.CharField( max_length=50)
    cast= models.CharField(max_length=50)
    type= models.CharField(max_length=50)
    budget= models.IntegerField()
    collection= models.IntegerField()
    streaming= models.CharField(max_length=50)
    rating= models.IntegerField()