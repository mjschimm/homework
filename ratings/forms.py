from django import forms
from ratings.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['beer_name', 'score', 'notes', 'brewery']
