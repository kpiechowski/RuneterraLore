from django.contrib import admin
from .models import Region, Champion
# Register your models here.


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
	list_display = ['name', 'champions_count']


@admin.register(Champion)
class RegionAdmin(admin.ModelAdmin):
	list_display = ['name']