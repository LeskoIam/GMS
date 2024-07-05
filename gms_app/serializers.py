from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Garden, GardenBed, Plant, Planting


class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ("pk", "name", "description")


class GardenBedSerializer(serializers.ModelSerializer):
    garden = GardenSerializer(read_only=True)

    class Meta:
        model = GardenBed
        fields = ("pk", "garden", "name", "description", "location")


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ("pk", "name", "description", "garden_beds")


class PlantingSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(read_only=True)
    garden_bed = GardenBedSerializer(read_only=True)

    class Meta:
        model = Planting
        fields = ("plant", "garden_bed", "location", "planting_date")


class GardenDetailsSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""

    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()

    garden_beds = SerializerMethodField()  # implicitly `get_garden_beds`

    def get_garden_beds(self, instance):
        """Return nested details about garden beds."""
        return [
            {
                "name": garden_bed.name,
                "description": garden_bed.description,
                "location": garden_bed.location,
                "plants": [
                    {
                        "pk": planting.plant.pk,
                        "pk_planting": planting.pk,
                        "name": planting.plant.name,
                        "description": planting.plant.description,
                        "location": str(planting.location),
                    }
                    for planting in Planting.objects.filter(garden_bed=garden_bed)
                ],
            }
            for garden_bed in GardenBed.objects.filter(garden=instance)
        ]
