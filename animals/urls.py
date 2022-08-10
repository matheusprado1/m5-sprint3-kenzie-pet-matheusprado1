from django.urls import path
from . views import AnimalView, AnimalViewById

urlpatterns = [
    path("animals/", AnimalView.as_view()),
    path("animals/<int:id>", AnimalViewById.as_view()),
]