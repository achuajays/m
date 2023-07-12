from django.shortcuts import render
from .models import music 
# Create your views here.

def musicc(request):
    form = music.objects.all()
    return render ( request , 'app/music.html'    , { 'form' : form } )
