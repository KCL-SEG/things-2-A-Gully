from django import forms
from .models import Thing
"""Forms of the project."""

# Create your forms here.


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        exclude = ('created_at')
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput()
        }
