from django.shortcuts import render
from django.views.generic import FormView, ListView, TemplateView, View

from gms_app.models import Garden, GardenBed, Plant


# Create your views here.
class GardenHomeView(TemplateView):
    template_name = "home.html"


class GardenListView(ListView):
    model = Garden
    template_name = "garden_list.html"


class GardenDetailView(View):
    # dartmouth = GardenBed.objects.get(garden_id=)
    # dartmouth.student_set.all()  # returns all students at Dartmouth
    # dartmouth.objects.filter(student__first_name='william')  # returns all Dartmouth students named William

    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        garden = Garden.objects.get(pk=pk)
        beds = GardenBed.objects.filter(garden=garden)
        plants = {bed: Plant.objects.filter(garden_bed=bed) for bed in beds}
        return render(request, "garden_detail.html", {"garden": garden, "beds": beds, "plants": plants})


# class AddPlantView(FormView):
#     template_name = "add_plant_form.html"
#     form_class = AddPlantForm
#     success_url = "/garden/garden"
#
#     def form_valid(self, form):
#         """This method is called when valid form data has been posted
#         Returns:
#             HttpResponse
#         """
#         p = Plant(name=form.cleaned_data["plant_name"], description=form.cleaned_data["plant_description"])
#         p.save()
#         return super().form_valid(form)
