from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .serializer import HeroSerializer, CompanySerializer, PowerStatsSerializer
from .models.models import Hero, Company, Power_stats


@api_view(["GET", "POST"])
@csrf_exempt
def hero_list(request):

    if request.method == "GET":
        hero = Hero.objects.all()
        serializer = HeroSerializer(hero, many=True)
        return Response({"data": serializer.data})

    elif request.method == "POST":
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def company_list(request):

    if request.method == "GET":
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response({"data": serializer.data})

    elif request.method == "POST":
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def power_list(request):

    if request.method == "GET":
        power_stats = Power_stats.objects.all()
        serializer = PowerStatsSerializer(power_stats, many=True)
        return Response({"data": serializer.data})

    elif request.method == "POST":
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def hero_detail(request):
    id = request.query_params["id"]

    try:
        hero = Hero.objects.get(id=id)
    except Hero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HeroSerializer(hero, many=False)
        return Response({"data": serializer.data})

    elif request.method == "PUT":
        serializer = HeroSerializer(hero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "PUT", "DELETE"])
def company_detail(request):
    id = request.query_params["id"]

    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CompanySerializer(company, many=False)
        return Response({"data": serializer.data})

    elif request.method == "PUT":
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
