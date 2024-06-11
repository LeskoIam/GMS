# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

from django.forms import BooleanField, CheckboxInput, ModelForm, Textarea, TextInput

from .models import Plant


class AddPlantForm(ModelForm):
    # save_plant_preset = BooleanField(widget=CheckboxInput(
    #     attrs={'id': 'flexCheckDefault', "class": "form-check-input", "type": "checkbox", "checked": ""}),
    #     label="Save Plant Preset"
    # )
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
            # "save_preset_plant": BooleanField(initial=True, required=False),
        }
