from django.db import models
import uuid

class Note(models.Model):
   
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    title = models.CharField(max_length=200,blank=False)
    text =  models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    