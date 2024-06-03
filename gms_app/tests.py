import logging

import pytest
from django.db.utils import IntegrityError

from gms_app import models

log = logging.getLogger(__name__)


@pytest.fixture(scope="module", autouse=True)
def _prepare_db(django_db_setup, django_db_blocker):
    # Set up non-modified objects used by all test methods
    with django_db_blocker.unblock():
        garden = models.Garden.objects.create(name="Test Garden", description="Test Garden Description")
        garden_bed = models.GardenBed.objects.create(
            garden=garden, name="Test Garden Bed", description="Test Garden Bed Description 1"
        )
        log.info("Garden '%s' - garden bed '%s'", garden.name, garden_bed.name)
        for plant_i in range(3):
            p = models.Plant(name=f"Test Plant {plant_i}", description=f"Test Plant Description{plant_i}")
            p.save()
            p.garden_bed.add(garden_bed)
            log.info("\tAdded plant '%s'", p.name)


@pytest.mark.django_db()
def test_numer_of_garden_beds():
    """Number of garden beds for garden is correct."""
    garden = models.Garden.objects.get(name="Test Garden")
    beds = models.GardenBed.objects.filter(garden=garden)

    assert len(beds) == 1


@pytest.mark.django_db()
def test_number_of_plants():
    """Number of plants for garden bed is correct."""
    garden = models.Garden.objects.get(name="Test Garden")
    beds = models.GardenBed.objects.filter(garden=garden)
    plants = models.Plant.objects.filter(garden_bed=beds[0])

    assert len(plants) == 3


@pytest.mark.django_db()
def test_allow_same_plant_on_bed():
    """We need to be able to have multiples of plants on the same garden bed.

    Given garden with garden beds
      And garden bed has one "Test Plant 1" plant already
    When we add another "Test Plant 1" plant on the same garden bed
    Then it should add the plant to the garden bed
    """
    garden = models.Garden.objects.get(name="Test Garden")
    beds = models.GardenBed.objects.filter(garden=garden)
    plant = models.Plant(name="Test Plant 1", description="Test Garden Bed Description")
    try:
        plant.save()  # <-- This will raise IntegrityError
        plant.garden_bed.add(beds)
    except IntegrityError:
        pytest.fail("Couldn't save the plant. Only one unique plant per garden STILL allowed!", pytrace=True)
