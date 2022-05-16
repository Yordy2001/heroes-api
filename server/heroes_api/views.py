from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models.heroes_stats import Hero, Company, Power_stats
from .models.user import User
from .serializer import HeroSerializer, CompanySerializer, PowerStatsSerializer
from .serializer import UserSerializer

# Create your views here.
@api_view(["GET", "POST"])
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


@api_view(["GET"])
def get_one_hero(request):
    id = request.query_params["id"]

    try:
        if request.method == "GET":
            hero = Hero.objects.filter(id=id)
            serializer = HeroSerializer(hero, many=False)
            return Response({"data": serializer.data})
    except Exception as e:
        print(id)
        raise e


@api_view(["GET"])
def get_one_company(request):
    id = request.query_params["id"]
    if request.method == "GET":
        company = Company.objects.filter(id=id)
        serializer = CompanySerializer(company, many=False)
        return Response({"data": serializer.data})


@api_view(['POST'])
def login(request):
    password = request.data['password']

    try: 
        user = User.objects.get(email=request.data['email'])
        serializer = UserSerializer(user, many=False)
        if password == serializer.data['password']:
            return Response(status=status.HTTP_200_OK)
    except Exception as e: 
        raise e

@api_view(["POST"])
def register(request):

    try:
        user = User.objects.get(email=request.data['email'])
        if user:
            return Response("Este correo pertenece a un usuario", status=status.HTTP_208_ALREADY_REPORTED)
    except User.DoesNotExist:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
