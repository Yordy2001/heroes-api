from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models.models import Hero, Company, Power_stats, User


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ["name", "image", "description", "video"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["hero", "name", "logo", "info", ]


class PowerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power_stats
        fields = ["hero", "intelligence", "strength",
                  "speed", "durability", "power", "combat"]


class UserSerializer(serializers.ModelSerializer):
    class MetaL:
        model = User
        fields = ["user_name", "email", "password", "permission"]
