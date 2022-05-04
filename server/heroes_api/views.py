from django.shortcuts import render
from django.http import JsonResponse
from .serializer import HeroSerializer, CompanySerializer, PowerStatsSerializer
from .models import Hero, Company, Power_stats

# Create your views here.
def hero_list(request):
    
    hero = Hero.objects.all()
    serializer = HeroSerializer(hero, many=True)
    return JsonResponse({"data":serializer.data}, safe=False)

def company_list(request):

    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return JsonResponse({ "data": serializer.data}, safe=False )

def power_list(request):
    power_stats = Power_stats.objects.all()
    serializer = CompanySerializer(power_stats, many=True)
    return JsonResponse({ "data": serializer.data}, safe=False )
