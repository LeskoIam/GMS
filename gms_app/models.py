from django.db import models


class Garden(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class GardenBed(models.Model):
    garden = models.ForeignKey(Garden, blank=True, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class Plant(models.Model):
    garden_bed = models.ManyToManyField(GardenBed, blank=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    location = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class PlantPreset(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
