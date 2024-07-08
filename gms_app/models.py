from datetime import datetime

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import QuerySet


class NoteCategory(models.Model):
    name = models.CharField(
        max_length=32, verbose_name="Note category name", help_text="Enter note category name", unique=True
    )
    acronym = models.CharField(
        max_length=5, verbose_name="Acronym", help_text="Enter note category acronym", unique=True
    )
    description = models.CharField(
        max_length=127,
        verbose_name="Note category description",
        help_text="Enter note category description",
        unique=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Note Category"
        verbose_name_plural = "Note Categories"
        ordering = ["acronym"]

    def __str__(self):
        return self.name


class Note(models.Model):
    foreign_table = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, help_text="Select on which model to place note"
    )
    # Key (Id) of the row in `content_type` table
    foreign_table_key = models.PositiveIntegerField(help_text="Input key (id) of the data in foreign_table")
    content_object = GenericForeignKey("foreign_table", "foreign_table_key")

    title = models.CharField(max_length=32, verbose_name="Note title", help_text="Enter note title")
    text = models.TextField(blank=True, help_text="Enter note text")
    date = models.DateTimeField(
        default=datetime.now, verbose_name="Date of the note", help_text="Enter the date of the note", null=True
    )
    category = models.ManyToManyField(NoteCategory, related_name="notes", blank=True, help_text="Select note category")

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        ordering = ["date"]

    def __str__(self):
        return f"{self.title} on {self.foreign_table} - {self.foreign_table_key}"


class Garden(models.Model):
    name = models.CharField(max_length=50, verbose_name="Garden Name", help_text="Enter the name of the garden")
    description = models.TextField(blank=True, help_text="Enter a brief description of the garden")
    note = GenericRelation(Note)

    class Meta:
        verbose_name = "Garden"
        verbose_name_plural = "Gardens"
        ordering = ["name"]

    def __str__(self):
        return self.name

    # def add_note(self, title, text, date, category):
    #     Note.objects.create(
    #         foreign_table=self, foreign_table_key=self.pk, title=title, text=text, date=date, category=category
    #     )


class GardenBed(models.Model):
    garden = models.ForeignKey(
        Garden,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="beds",
        help_text="Select the garden this bed belongs to",
    )
    name = models.CharField(max_length=100, verbose_name="Bed Name", help_text="Enter the name of the garden bed")
    description = models.TextField(blank=True, help_text="Enter a brief description of the garden bed")
    location = models.JSONField(
        default=dict, help_text="Enter the location of the garden bed in garden as a JSON object"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Garden Bed"
        verbose_name_plural = "Garden Beds"
        ordering = ["name"]

    def add_plant(self, plant: "Plant", location: dict[str : int | float, str : int | float]) -> "Planting":
        """Add Plant to this GardenBed.

        :param plant: Plant to be added.
        :param location: Where the plant is located on this garden bed.
        :return: Planting object.
        """
        return Planting.objects.create(
            plant=plant,
            garden_bed=self,
            location=location,
        )

    def get_plantings(self) -> QuerySet:
        """Get Planting objects for this GardenBed.

        :return: Planting objects for this GardenBed.
        """
        return self.plantings.filter(garden_bed=self)


class Plant(models.Model):
    """Represents the Plant "type" that can exist outside a plant bed."""

    # The name being unique causes a unique constraint error if we do a direct
    # many-to-many relationship with the garden bed
    name = models.CharField(
        max_length=50, unique=True, verbose_name="Plant Name", help_text="Enter the name of the plant"
    )
    description = models.TextField(blank=True, help_text="Enter a brief description of the plant")
    garden_beds = models.ManyToManyField(
        GardenBed,
        through="Planting",
        blank=True,
        related_name="plants",
        help_text="Select the garden beds where this plant is located",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plant"
        verbose_name_plural = "Plants"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        """Also save PlantPreset if entered plant is not already present in PlantPreset table."""
        super().save(*args, **kwargs)
        PlantPreset.objects.get_or_create(name=self.name, defaults={"description": self.description})

    def get_plantings(self, garden_bed: GardenBed, location) -> QuerySet:
        """Get Planting objects for this Plant.

        :return: Planting objects for this Plant.
        """
        pl = self.plantings.filter(plant=self, garden_bed=garden_bed, location=location)
        return pl


class Planting(models.Model):
    """Represents the plant in the garden bed.

    This is a join model between the plant "type" and it's "instance" in a garden bed
    """

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="plantings")
    garden_bed = models.ForeignKey(GardenBed, on_delete=models.CASCADE, related_name="plantings")
    # moved location from Plant to Planting
    location = models.JSONField(
        default=dict, help_text="Enter the location of the plant in the garden bed as a JSON object"
    )
    planting_date = models.DateField(
        verbose_name="Planting date", help_text="Enter the date of the planting", blank=True, null=True
    )

    def __str__(self):
        return f"{self.plant.name} in {self.garden_bed.name} at {self.location}"

    class Meta:
        unique_together = [["garden_bed", "location"]]
        verbose_name = "Planting"
        verbose_name_plural = "Plantings"


class PlantPreset(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plant preset"
        verbose_name_plural = "Plant presets"
        ordering = ["name"]
