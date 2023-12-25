from django.shortcuts import render
from .forms import DiceForm
import random


def roll_dice_view(request):
    # Check if the request method is POST
    if request.method == "POST":
        form = DiceForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # If valid, get the number of sides and dice from the form data
            sides = form.cleaned_data["sides"]
            num_dice = form.cleaned_data["num_dice"]
            # Generate a list of random numbers, each between 1 and the number of sides
            results = [random.randint(1, sides) for _ in range(num_dice)]
            # Render the template with the form and results
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
        # If the request method is not POST, create a new form
        form = DiceForm()
    # Render the template with the form
    return render(request, "dices/roll_dice.html", {"form": form})
