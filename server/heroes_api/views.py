from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def index(request):
    return HTTPResponse("Hello, Word!")
