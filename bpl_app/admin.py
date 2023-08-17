from django.contrib import admin

# Register your models here.
from bpl_app.models import TeamsInfo,Matches

admin.site.register(TeamsInfo)
admin.site.register(Matches)
