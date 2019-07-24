from django.shortcuts import render
import datetime
from django.http import *
from api.models import Sms

# Create your views here.


def home(request):
    # sms = Sms.objects.get(Sms_ID=1)
    # sms.IsProcessed = True
    # sms.save()
    # # sms.IsProcessed = True
    # return HttpResponse(str(sms.IsProcessed))
    return HttpResponseNotFound("<h1 style='text-align:center;position:absolute;width:100%;top:40%;'>404 - Not Found</h1>")
