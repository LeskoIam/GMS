import logging

import pytest
from django.db.utils import IntegrityError


from gms_app.models import Garden, GardenBed, Plant, Planting

log = logging.getLogger(__name__)


@pytest.fixture(scope="module", autouse=True)
def _prepare_db(django_db_setup, django_db_blocker):
    # Set up non-modified objects used by all test methods
    with django_db_blocker.unblock():
        garden = Garden.objects.create(
            name="Test Garden",
            description="Test Garden Description",
        )
        garden_bed = GardenBed.objects.create(
            garden=garden,
            name="Test Garden Bed",
            description="Test Garden Bed Description 1",
        )
        log.info("Garden '%s' - garden bed '%s'", garden.name, garden_bed.name)
        for plant_i in range(3):
            plant = Plant.objects.create(
                name=f"Test Plant {plant_i}",
                description=f"Test Plant Description{plant_i}",
            )
            planting = Planting.objects.create(
                plant=plant,
                garden_bed=garden_bed,
                location={"x": plant_i, "y": 0},
            )
            log.info("\tAdded plant '%s'", plant.name)


@pytest.mark.django_db()
def test_numer_of_garden_beds():
    """Number of garden beds for garden is correct."""
    garden = Garden.objects.get(name="Test Garden")
    beds = GardenBed.objects.filter(garden=garden)

    assert len(beds) == 1


@pytest.mark.django_db()
def test_number_of_plant_in_first_garden_bed():
    """Number of plants for garden bed is correct."""
    garden = Garden.objects.get(name="Test Garden")
    garden_bed = GardenBed.objects.filter(garden=garden).first()
    plants = garden_bed.plants.all()
    assert len(plants) == 3
    # or simply
    # assert garden_bed.plants.count() == 3


@pytest.mark.django_db()
def test_allow_duplicate_plants_on_bed():
    """We need to be able to have multiples of plants on the same garden bed.

    Given garden with garden beds
      And garden bed has one "Test Plant 1" plant already
    When we add another "Test Plant 1" plant on the same garden bed
    Then it should add the plant to the garden bed
    """
    garden = Garden.objects.get(name="Test Garden")
    plant = Plant.objects.first()
    # Brittle. Assumes knowledge of the locations in the model factory fixture
    location = {"x": 3, "y": 0}

    for bed in GardenBed.objects.filter(garden=garden):
        planting = bed.add_plant(plant, location)
        assert planting.plant == plant
        assert planting.location == location
