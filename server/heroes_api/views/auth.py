from django.http import HttpResponse
from urllib import request
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from ..serializer import UserSerializer
from ..models.models import User


@api_view(["POST"])
@csrf_exempt
def login(request):

    if request.method == "POST":
        if request.data.email and request.data.password:
            return Response(status=status.HTTP_200_OK)
        return Response(request.data)


@csrf_exempt
@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    user = User.objects.get(email=request.data.email)
    if user:
        return Response(status=status.HTTP_303_SEE_OTHER)

    elif serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
