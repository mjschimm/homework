from django import forms
from ratings.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['beer_name', 'score', 'notes', 'brewery']
        widgets = {
            'beer_name': forms.TextInput(attrs={'size': '35'}),
            'brewery': forms.TextInput(attrs={'size': '35'}),
            'notes': forms.Textarea(attrs={'rows':5, 'cols':35}),
            'score': forms.NumberInput(attrs={'cols':5}),
        }
