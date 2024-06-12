# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

from django.forms import BooleanField, CheckboxInput, ChoiceField, ModelForm, Select, Textarea, TextInput

from .models import Plant, Planting


class AddPlantForm(ModelForm):
    add_plant_to_planting = BooleanField(
        widget=CheckboxInput(attrs={"id": "flexCheckDefault", "class": "form-check-input", "type": "checkbox"}),
        label="Add Plant to Planting",
        required=False,
    )

    class Meta:
        model = Plant
        fields = ["name", "description"]
        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "id": "exampleFormControlInput1", "placeholder": "Enter your plant name"}
            ),
            "description": Textarea(
                attrs={
                    "class": "form-control",
                    "id": "exampleFormControlTextarea1",
                    "rows": "3",
                    "placeholder": "Enter your plant description",
                }
            ),
        }


class AddPlantToGardenBedForm(ModelForm):
    class Meta:
        model = Planting
        fields = ["plant", "garden_bed", "location"]
        widgets = {
            "plant": Select(attrs={"class": "form-select", "size": "7", "aria-label": "size 7 select example"}),
            "garden_bed": Select(attrs={"class": "form-select", "size": "4", "aria-label": "size 4 select example"}),
        }
        # attrs={"class": "form-select", "size": "7", "multiple": None, "aria-label": "multiple size 7 select example"}
