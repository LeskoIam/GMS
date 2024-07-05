from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from gms_app.models import Garden, GardenBed, Plant, Planting
from gms_app.serializers import (
    GardenBedSerializer,
    GardenDetailsSerializer,
    GardenSerializer,
    PlantSerializer,
)


@api_view(["GET", "POST"])
def garden_list(request) -> Response:
    """List of all Gardens."""
    if request.method == "GET":
        data = Garden.objects.all()

        serializer = GardenSerializer(data, context={"request": request}, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = GardenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def garden_bed_list(request) -> Response:
    """List of all GardensBeds."""
    if request.method == "GET":
        data = GardenBed.objects.all()

        serializer = GardenBedSerializer(data, context={"request": request}, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = GardenBedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def plant_list(request) -> Response:
    """List of all Plants."""
    if request.method == "GET":
        data = Plant.objects.all()

        serializer = PlantSerializer(data, context={"request": request}, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def garden_details(request, pk) -> Response:
    """List of all Plants."""
    if request.method == "GET":
        garden = Garden.objects.filter(pk=pk)
        if garden.exists():
            serializer = GardenDetailsSerializer(garden.first(), context={"request": request})

            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
