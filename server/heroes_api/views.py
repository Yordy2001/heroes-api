import imp
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse

from .models import Hero

# Create your views here.
def index(request):
    print(Hero.objects.all())

    return JsonResponse({"data":list(Hero.objects.all())})
