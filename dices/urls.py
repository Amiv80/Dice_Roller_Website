from django.urls import path
from . import views

urlpatterns = [
    path("roll/", views.roll_dice_view, name="roll_dice"),
]
