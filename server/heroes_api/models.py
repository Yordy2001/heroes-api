from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=70)
    image = models.CharField(max_length=70)
    description = models.TextField()
    video = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name, self.description

class Company(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=70)
    info = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering =['name']

class Power_stats(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    intelligence = models.PositiveBigIntegerField()
    strength = models.PositiveBigIntegerField()
    speed = models.PositiveBigIntegerField()
    durability = models.PositiveBigIntegerField()
    power = models.PositiveBigIntegerField()
    combat = models.PositiveBigIntegerField()
    date_added = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.intelligence, self.strength, self.power