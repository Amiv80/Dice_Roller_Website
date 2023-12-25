from django import forms


class DiceForm(forms.Form):
    sides = forms.IntegerField(min_value=1, required=True)
    num_dice = forms.IntegerField(min_value=1, required=True)
