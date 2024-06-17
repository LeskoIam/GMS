from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import FormView, ListView, TemplateView, View

from gms_app.forms import AddPlantForm, AddPlantToGardenBedForm
from gms_app.models import Garden, GardenBed, Plant, Planting


class GardenHomeView(TemplateView):
    template_name = "home.html"


class GardenListView(ListView):
    model = Garden
    template_name = "garden_list.html"


class GardenDetailView(View):
    def get(self, request, *args, **kwargs):
        """Show "tree view" for given Garden."""
        pk = kwargs["pk"]
        garden = Garden.objects.get(pk=pk)
        beds = GardenBed.objects.filter(garden=garden)
        plantings = {bed: bed.get_plantings() for bed in beds}
        return render(request, "garden_detail.html", {"garden": garden, "beds": beds, "plantings": plantings})


class AddPlantView(FormView):
    template_name = "forms/add_plant_form.html"
    form_class = AddPlantForm
    success_url = "/garden/garden"

    def form_valid(self, form):
        """Called when valid form data has been posted
        Returns:
            HttpResponse
        """
        p = Plant(name=form.cleaned_data["name"], description=form.cleaned_data["description"])
        p.save()
        if form.cleaned_data["add_plant_to_planting"]:
            return HttpResponseRedirect(reverse("add_plant_to_bed"))
        return super().form_valid(form)


class AddPlantToGardenBedView(FormView):
    template_name = "forms/add_plant_to_garden_bed_form.html"
    form_class = AddPlantToGardenBedForm
    success_url = "/garden/garden"

    def form_valid(self, form):
        """Called when valid form data has been posted
        Returns:
            HttpResponse
        """
        p = Planting(
            plant=form.cleaned_data["plant"],
            garden_bed=form.cleaned_data["garden_bed"],
            location=form.cleaned_data["location"],
            planting_date=form.cleaned_data["planting_date"],
        )
        p.save()
        return super().form_valid(form)
