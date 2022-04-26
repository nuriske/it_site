from django.contrib import admin
from .models import Info


class InfoAdnin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')

admin.site.register(Info, InfoAdnin)
