from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=70)
    image = models.CharField(max_length=70)
    description = models.TextField()
    video = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} {} '.format(self.name, self.description)

class Company(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=70)
    info = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.name, self.hero)

    class Meta:
        ordering =['name']

class Power_stats(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    intelligence = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    strength = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    speed = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    durability = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    power = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    combat = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.intelligence, self.strength, self.power)
