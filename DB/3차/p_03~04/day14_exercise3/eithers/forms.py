from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    issue_a = forms.CharField(label="RED TEAM")
    issue_b = forms.CharField(label="BLUE TEAM")
    class Meta:
        model = Question
        fields = '__all__'


class CommentForm(forms.ModelForm):
    TEAM_A = '0'
    TEAM_B = '1'
    TEAM_CHOICES = [
        (TEAM_A, 'RED TEAM'),
        (TEAM_B, 'BLUE TEAM'),
    ]
    pick = forms.ChoiceField(choices=TEAM_CHOICES)

    class Meta:
        model = Comment
        exclude = ['question',]