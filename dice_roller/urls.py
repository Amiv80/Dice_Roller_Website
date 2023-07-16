from django.urls import path
from dices.views import roll_dice_view

urlpatterns = [
    path('', roll_dice_view, name='roll_dice'),
]