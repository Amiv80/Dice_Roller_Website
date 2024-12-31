from django.shortcuts import render
import random
import re


def roll_dice(sides, num_rolls=1):
    return [random.randint(1, sides) for _ in range(num_rolls)]


def parse_dice_input(num_rolls, dice_type, modifier_input):
    try:
        num_rolls = int(num_rolls)
        dice_type = (
            int(dice_type) if dice_type != "custom" else int(modifier_input)
        )  # Custom dice input handled here
        modifier = int(modifier_input) if modifier_input else 0
        return num_rolls, dice_type, modifier
    except ValueError:
        raise ValueError(
            "Invalid input, please provide valid numbers for rolls and modifiers."
        )


def roll_dice_view(request):
    results = None
    if request.method == "POST":
        try:
            num_rolls = request.POST.get("num_rolls", 1)
            dice_type = request.POST.get("dice_type", 6)
            modifier_input = request.POST.get("modifier", 0)
            custom_dice_input = request.POST.get("custom_dice", 0)

            # If custom dice is selected, we need to use the custom value
            if dice_type == "custom":
                dice_type = custom_dice_input

            # Parse inputs
            num_rolls, dice_type, modifier = parse_dice_input(
                num_rolls, dice_type, modifier_input
            )

            # Roll the dice
            rolls = roll_dice(dice_type, num_rolls)
            total = sum(rolls) + modifier

            results = {
                "success": True,
                "rolls": rolls,
                "total": total,
                "modifier": modifier,
            }
        except ValueError as e:
            results = {
                "success": False,
                "error": str(e),
            }

    return render(
        request,
        "dices/roll_dice.html",
        {
            "results": results,
            "dice_type": request.POST.get("dice_type", "6"),
            "modifier": request.POST.get("modifier", ""),
        },
    )
