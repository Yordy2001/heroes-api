from dataclasses import fields
from pydoc import importfile
from pyexpat import model
from rest_framework  import serializers

from .models.heroes_stats import Hero, Company, Power_stats
from .models.user import User

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = [ "name", "image", "description", "video" ]

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [ "hero", "name", "logo", "info", ]

class PowerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power_stats
        fields = [ "hero", "intelligence", "strength", "speed", "durability", "power", "combat" ]

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = [ "user_name", "email", "password", "permission"]