from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    
    noteId = serializers.UUIDField(source='id',read_only=True)
    content = serializers.CharField(source='text')
    lat = serializers.FloatField(source='latitude')
    lng = serializers.FloatField(source='longitude')

    class Meta:
        model = Note
        fields = ['noteId','title','content','lat','lng','date']
        

class NoteListSerializer(serializers.ModelSerializer):
    lat = serializers.FloatField(source='latitude')
    lng = serializers.FloatField(source='longitude')
    
    class Meta:
        model = Note
        fields = ['id','lat','lng']