from django.shortcuts import render
import random

def roll_dice_view(request):
    if request.method == 'POST':
        sides = request.POST.get('sides')
        num_dice = request.POST.get('num_dice')
        roll_again = request.POST.get('roll_again')

        if roll_again:
            sides = request.session.get('sides')
            num_dice = request.session.get('num_dice')
        else:
            request.session['sides'] = sides
            request.session['num_dice'] = num_dice

        if not sides or not num_dice:
            return render(request, 'dices/roll_dice.html', {'error': 'Please enter a valid input.'})

        try:
            sides = int(sides)
            num_dice = int(num_dice)
        except ValueError:
            return render(request, 'dices/roll_dice.html', {'error': 'Please enter valid integers.'})

        results = []
        current_round = []
        for i in range(1, num_dice + 1):
            dice_result = random.randint(1, sides)
            current_round.append(dice_result)
        results.append(current_round)

        return render(request, 'dices/roll_dice.html', {'results': results})

    return render(request, 'dices/roll_dice.html')