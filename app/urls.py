from django.urls import path 
from  . import views 


urlpatterns = [
    path('',views.musicc,name="music"),
]