from django.shortcuts import render

# Create your views here.
from app.models import *

from django.http import HttpResponse

def insertTopic(request):

    if request.method=='POST':
        tn=request.POST['tn']

    

        TO=Topic.objects.get_or_create(topic_name=tn)
        return HttpResponse(f'{tn} Topic is Created')


    return render(request,'insertTopic.html')