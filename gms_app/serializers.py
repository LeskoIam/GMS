from rest_framework import serializers

from .models import Garden, GardenBed, Plant, Planting


class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ("pk", "name", "description")


class GardenBedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GardenBed
        fields = ("pk", "garden", "name", "description", "location")


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ("pk", "name", "description", "garden_beds")


class PlantingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planting
        fields = ("pk", "plant", "garden_bed", "location", "planting_date")
