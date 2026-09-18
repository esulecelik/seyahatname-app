from django.core.management.base import BaseCommand
from note.models import Note
from django.utils import timezone
class Command(BaseCommand):
    help = 'Veritabanına not verileri ekler'
    
    def handle(self, *args, **kwargs):
        
        notes = [
            Note(title="Üniversite Hazırlık",text="Burada Zehra,Selin,Rabia ile tanıştım.",latitude=41.000122,longitude=28.859788,date=timezone.now())
        ]
        
        Note.objects.bulk_create(notes) 