from django.contrib import admin

# Register your models here.
from django.contrib import admin
from forecast_app.models import UserProfile, Team, Match, League, Tournament

admin.site.register(UserProfile)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(League)
admin.site.register(Tournament)
