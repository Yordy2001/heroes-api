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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "user_name", "email", "password", "permission"]