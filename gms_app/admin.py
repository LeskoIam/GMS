from django.contrib import admin

from .models import Garden, GardenBed, Plant, PlantPreset

admin.site.register(Garden)
admin.site.register(GardenBed)
admin.site.register(Plant)
admin.site.register(PlantPreset)
