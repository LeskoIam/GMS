import logging

import pytest
from django.db.utils import IntegrityError

from gms_app.models import Garden, GardenBed, Plant, Planting

log = logging.getLogger(__name__)


@pytest.fixture(scope="module", autouse=True)
def _prepare_db(django_db_setup, django_db_blocker):
    """Set up non-modified objects used by all test methods"""
    with django_db_blocker.unblock():
        # Create 1 Garden
        garden = Garden.objects.create(
            name="Test Garden",
            description="Test Garden Description",
        )

        # Create 2 GardenBeds
        garden_bed_0 = GardenBed.objects.create(
            garden=garden,
            name="Test Garden Bed 1",
            description="Test Garden Bed Description 1",
        )
        garden_bed_1 = GardenBed.objects.create(
            garden=garden,
            name="Test Garden Bed 2",
            description="Test Garden Bed Description 2",
        )
        log.info("\tGarden '%s' - garden_bed_0 '%s'", garden.name, garden_bed_0.name)
        log.info("\tGarden '%s' - garden_bed_1 '%s'", garden.name, garden_bed_1.name)

        # Create 2 Plants
        plant_0 = Plant.objects.create(
            name="Test Plant 1",
            description="Test Plant Description 1",
        )
        plant_1 = Plant.objects.create(
            name="Test Plant 2",
            description="Test Plant Description 2",
        )
        log.info("\t\tAdded plant_0 '%s'", plant_0.name)
        log.info("\t\tAdded plant_1 '%s'", plant_1.name)

        # Add plant_0 to garden_bed_0
        garden_bed_0.add_plant(plant_0, location={"x": 0, "y": 0})
        log.info("\t\tAdded plant_0 '%s' to '%s'", plant_0.name, garden_bed_0)


@pytest.mark.django_db()
def test_number_of_garden_beds():
    """Number of garden beds for garden is correct."""
    garden = Garden.objects.get(name="Test Garden")
    beds = GardenBed.objects.filter(garden=garden)
    assert beds.count() == 2


@pytest.mark.django_db()
def test_number_of_plant_in_first_garden_bed():
    """Number of plants for garden bed is correct."""
    garden = Garden.objects.get(name="Test Garden")
    garden_bed = GardenBed.objects.filter(garden=garden).first()
    assert garden_bed.plants.count() == 1


@pytest.mark.django_db()
def test_allow_duplicate_plants_on_bed():
    """We need to be able to have multiples of plants on the same garden bed.

    Given garden with garden beds
      And garden bed has one "Test Plant 1" plant already at location (0, 0)
    When we add another "Test Plant 1" plant on the same garden bed but at different location
    Then it should add the plant to the garden bed
    """
    garden = Garden.objects.get(name="Test Garden")
    log.info("Garden: %s", garden)

    plant = Plant.objects.first()
    log.info("Plant to add: %s\n", plant)

    # New plant location
    location = {"x": 1, "y": 1}

    garden_bed = GardenBed.objects.get(garden=garden, name="Test Garden Bed 1")
    new_planting = garden_bed.add_plant(plant, location)

    assert new_planting.location == location
    assert new_planting.plant == plant
    assert bool(Planting.objects.filter(garden_bed=garden_bed, plant=plant, location=location))


@pytest.mark.django_db()
def test_one_location_can_only_have_one_plant():
    """Only one plant can be planted at the same location on garden bed.

    Given garden with garden beds
      And garden bed has one "Test Plant 1" plant at location (0, 0) already
    When we add new "Test Plant 77" plant on the same garden bed at location (0, 0)
    Then it should not save to database
    """
    garden = Garden.objects.get(name="Test Garden")
    log.info("Garden: %s", garden)

    plant = Plant.objects.create(
        name="Test Plant 77",
        description="Test Plant Description 77",
    )
    log.info("Plant to add: %s\n", plant)

    # New plant location
    location = {"x": 0, "y": 0}

    garden_bed = GardenBed.objects.get(garden=garden, name="Test Garden Bed 1")
    with pytest.raises(IntegrityError):
        new_planting = garden_bed.add_plant(plant, location)
    log.info(new_planting)
