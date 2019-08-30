from django.shortcuts import render
import datetime
from django.http import *
from api.models import Sms

# Create your views here.

def home(request):
    return HttpResponseNotFound("<h1 style='text-align:center;position:absolute;width:99%;top:40%;'>404 - Not Found</h1>")
