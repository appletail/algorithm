from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '제주도',
            }
        )
    )

    class Meta:
        model = Travel
        fields = '__all__'