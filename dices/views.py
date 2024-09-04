from django.shortcuts import render
from django.contrib import messages
from .forms import DiceForm
import random


def roll_dice_view(request):
    if request.method == "POST":
        form = DiceForm(request.POST)
        if form.is_valid():
            sides = form.cleaned_data["sides"]
            num_dice = form.cleaned_data["num_dice"]

            if sides < 1 or num_dice < 1:
                messages.error(request, "Number of sides and dice must be at least 1.")
                return render(request, "dices/roll_dice.html", {"form": form})

            results = [random.randint(1, sides) for _ in range(num_dice)]
            return render(
                request,
                "dices/roll_dice.html",
                {
                    "form": form,
                    "results": results,
                    "sides": sides,
                    "num_dice": num_dice,
                },
            )
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = DiceForm()

    return render(request, "dices/roll_dice.html", {"form": form})
