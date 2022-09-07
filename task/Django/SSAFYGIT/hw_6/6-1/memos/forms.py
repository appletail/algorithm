from django import forms

class MemoForm(forms.Form):
    summary = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'summary',
            }
        )
    )

    memo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'memo',
                'cols': '50',
                'rows': '5',
            }
        )
    )
    