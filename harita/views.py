from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.conf import settings

class MapView(View):
    
    def dispatch(self, request, *args, **kwargs):
        self.template_name="harita/layout.html"
        self.map_api_key = settings.MAP_API_KEY
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
       return render(request, self.template_name,{
           'API_KEY' : self.map_api_key
       })