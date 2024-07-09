"""
URL configuration for gms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path

from gms_app.views import api_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("garden/", include("gms_app.urls")),
    # REST
    re_path(r"^api/gardens/$", api_views.garden_list),
    re_path(r"^api/beds/$", api_views.garden_bed_list),
    re_path(r"^api/plants/$", api_views.plant_list),
    re_path(r"^api/register/$", api_views.register_user),
    path("api/garden/<int:pk>/", api_views.garden_details),
    # re_path(r"^api/garden/$", api_views.garden_details),
]
