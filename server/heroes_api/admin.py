from django.contrib import admin

from .models.models import Hero, Company, Power_stats, User

# Register your models here.

admin.site.register(Hero)
admin.site.register(Company)
admin.site.register(Power_stats)
admin.site.register(User)
