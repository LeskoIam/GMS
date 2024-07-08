from django.contrib import admin

from .models import Garden, GardenBed, Note, NoteCategory, Plant, Planting, PlantPreset

admin.site.register(Garden)
admin.site.register(GardenBed)
admin.site.register(Plant)
admin.site.register(PlantPreset)
admin.site.register(Planting)
admin.site.register(Note)
admin.site.register(NoteCategory)
