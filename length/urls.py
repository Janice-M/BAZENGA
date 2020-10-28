from django.urls import path
from . import views

urlpatterns = [
    path('measurements/',views.MeasurementAPI.as_view(),
        name="measurements_api"),

]
