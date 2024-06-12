# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
from django.urls import path

from . import views

urlpatterns = [
    path("", views.GardenHomeView.as_view(), name="home"),
    path("garden/", views.GardenListView.as_view(), name="garden_list"),
    path("garden/<int:pk>/", views.GardenDetailView.as_view(), name="garden_detail"),
    path("garden/addplant/", views.AddPlantView.as_view(), name="add_plant"),
    path("garden/addplanttobed/", views.AddPlantToGardenBedView.as_view(), name="add_plant_to_bed"),
]
