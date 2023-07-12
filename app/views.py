from django.shortcuts import render
from .models import music 
# Create your views here.

def music(request):
    form = music.objects.all()
    return render ( request , 'app/music.html'    , { 'form' : form } )
