from rest_framework import views,status
from .models import Note
from rest_framework.response import Response
from .serializers import NoteListSerializer,NoteSerializer

class NoteListView(views.APIView):

    def get(self,request):
        notes = Note.objects.all()
        serializer = NoteListSerializer(notes,many=True)
        return Response(serializer.data)

class NoteView(views.APIView):
    
    def get(self,request,id):
        try:
            note = Note.objects.get(id=id)
        except Note.DoesNotExist:
            return Response({'detail': 'Not bulunamadı.'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = NoteSerializer(note)
        return Response(serializer.data)