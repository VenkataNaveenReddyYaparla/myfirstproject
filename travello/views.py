from django.shortcuts import render
from .models import Destination 
# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name='mumbai'
    dest1.desc='the city that never sleep '
    dest1.img ='destination_1.jpg'
    dest1.price =700

    dest2=Destination()
    dest2.name='hyderabad'
    dest2.desc='the city that never sleep '
    dest2.img ='destination_2.jpg'
    dest2.price =7020

    dests=[dest1,dest2]
    return render(request,"index.html",{'dests':dests})
