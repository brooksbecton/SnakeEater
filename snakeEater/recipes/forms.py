from django import forms


class NewRecipeForm(forms.Form):
    name = forms.CharField(label='Recipe Name', max_length=100)
    description = forms.CharField(label='Recipe Name', max_length=200)
    steps = forms.CharField(label='Recipe (CSV)',
                            max_length=300, widget=forms.Textarea)
