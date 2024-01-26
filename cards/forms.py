from .models import Card
from django import forms


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'body']
        labels = {'name': 'Name', 'body': 'Body'}
        widgets = {'body': forms.Textarea(attrs={'cols': 80, 'rows': 10})}
