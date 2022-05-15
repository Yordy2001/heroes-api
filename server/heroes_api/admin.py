from django.contrib import admin

from .models.heroes_stats import Hero, Company, Power_stats
from .models.user import User
# Register your models here.

admin.site.register(Hero)
admin.site.register(Company)
admin.site.register(Power_stats)
admin.site.register(User)
