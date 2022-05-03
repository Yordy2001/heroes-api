from django.contrib import admin

from .models import Hero, Company, Power_stats
# Register your models here.

admin.site.register(Hero)
admin.site.register(Company)
admin.site.register(Power_stats)
