from django.db import models

# def get_default_plant():
#     return PlantPreset.objects.get(name="default")


class Garden(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class GardenBed(models.Model):
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class PlantPreset(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Plant(PlantPreset):
    garden_bed = models.ManyToManyField(GardenBed, blank=True)

    def __str__(self):
        return self.name
