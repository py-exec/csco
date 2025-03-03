from django.urls import path
from .views import carton_form

urlpatterns = [
    path("carton-form/", carton_form, name="carton_form"),
]