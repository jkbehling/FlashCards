from django import forms
from django import forms
from flash_cards_app.models import Card, Deck

class CardForm(forms.ModelForm):
    
    card_image = forms.ImageField(required=False)
    clear_card_image = forms.BooleanField(required=False)

    class Meta:
        model = Card
        fields = ("front_content", "back_content", 'card_image',)

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ("name",)

class TestCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ("front_content",)

