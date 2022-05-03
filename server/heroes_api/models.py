from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=70)
    image = models.FieldFile()
    description = models.TextField()
    video = models.FieldFile()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name, self.description

class Company(models.models):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.FieldFile()
    info = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering =['name']

class Power_stats():
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    intelligence = models.PositiveBigIntegerField(max_length=100)
    strength = models.PositiveBigIntegerField(max_length=100)
    speed = models.PositiveBigIntegerField(max_length=100)
    durability = models.PositiveBigIntegerField(max_length=100)
    power = models.PositiveBigIntegerField(max_length=100)
    combat = models.PositiveBigIntegerField(max_length=100)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.intelligence, self.strength, self.power