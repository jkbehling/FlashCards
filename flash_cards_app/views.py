from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.utils.timezone import datetime
from flash_cards_app.forms import CardForm, DeckForm, TestCardForm
from flash_cards_app.models import Card, Deck
from django.views.generic import ListView
#from django.db.models import Max
# Create your views here.

app_name = 'flash_cards'

def home(request):
    form = CardForm(request.POST or None)
    cards = Card.objects.all()
    return render(request, "flashcards/home.html", {"form": form, "card_list": cards})


def about(request):
    return render(request, "flashcards/about.html")

def card_delete(request, id):
    card = Card.objects.get(id=id)
    deck = card.deck
    card.delete()
    #Renumber the remaining cards
    cardList = Card.objects.filter(deck=deck).order_by('card_num')
    for i in range(0, len(cardList)):
        cardList[i].card_num = i+1
        cardList[i].save()

    return redirect("view_deck", card.deck.id)

def deck(request):
    form = DeckForm(request.POST or None)
    decks = Deck.objects.all()

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("decks")

        else:
            return render(request, "flashcards/deck.html", {"form": form, "deck_list": decks})
    
    else:
        return render(request, "flashcards/deck.html", {"form": form, "deck_list": decks})

def deck_delete(request, id):
    deck = Deck.objects.get(id=id)
    deck.delete()
    return redirect("decks")

def view_deck(request, id):
    deck = Deck.objects.get(id=id)
    card_list = Card.objects.filter(deck=deck)
    if card_list.count() > 1:
        starting_card = card_list[0]
    else:
        starting_card = None

    form = CardForm(request.POST or None, request.FILES or None)
    request.META.get('HHTP_CUSTOM_HEADER')
    if request.method == "POST":
        if form.is_valid():
            card = form.save(commit=False)
            card.deck = deck
            card.save()
            return redirect("view_deck", id=id)

        else:
            return render(request, "flashcards/view_deck.html", {"deck": deck, "card_list": card_list, "form": form, "starting_card": card_list[0]})
    
    else:
        return render(request, "flashcards/view_deck.html", {"deck": deck, "card_list": card_list, "form": form, "starting_card": starting_card})

def card_list(request, id):
    deck = Deck.objects.get(id=id)
    card_list = Card.objects.filter(deck = deck)
    return render(request, "flashcards/card_list.html", { "card_list": card_list })

def card_Edit(request, id):
    card = Card.objects.get(id=id)
    if request.method == "POST":
        #deck = card.deck
        #card_list = Card.objects.filter(deck=deck)
        form = CardForm(request.POST, request.FILES or None, instance=card)
        
        if form.is_valid():
            #clearImage = form.cleaned_data['clear_card_image']
            if form.cleaned_data['clear_card_image'] == True:
                #card.card_image = ''
                card.card_image = None
            form.save()
            
            return HttpResponse(status=204, headers={'HX-Trigger': 'cardListChanged'})
            #return render(request, "flashcards/view_deck.html", {"deck": deck, "card_list": card_list, "form": form, "starting_card": card})
    else:
        form = CardForm(instance=card)

    return render(request, "flashcards/card_newEdit.html", {"form": form, "card": card, "deck": card.deck, "isNew": False})

def card_New(request, id):
    deck = Deck.objects.get(id=id)
    form = CardForm(request.POST or None, request.FILES or None)
    isNew = True
    if request.method == "POST":
        if form.is_valid():
            card = form.save(commit=False)

            cardList = Card.objects.filter(deck=deck)
            if cardList.count() > 0:
                #maxCardNum = cardList.aggregate(Max('card_num'))
                maxCardNum = Card.objects.filter(deck=deck).order_by('-id')[0].card_num
            else:
                maxCardNum = 0

            card.deck = deck
            card.card_num = maxCardNum + 1
            card.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'cardListChanged'})
        else:
            isNew = False

    return render(request, "flashcards/card_newEdit.html", {"form": form, "deck": deck, "isNew": isNew})

def carousel(request):
    return render(request, "flashcards/carousel.html")

def deck_new(request):
    form = DeckForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'deckListChanged'})
    return render(request, "flashcards/deck_newEdit.html", {"form": form })

def deck_edit(request, id):
    deck = Deck.objects.get(id=id)
    if request.method == "POST":
        form = DeckForm(request.POST, instance=deck)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'deckListChanged'})
    else:
        form = DeckForm(instance=deck)

    #Show view on first click; or if form isn't valid, return the popup page with errors
    return render(request, "flashcards/deck_newEdit.html", {"form": form, "deck": deck})

def deck_list(request):
    deck_list = Deck.objects.all()
    deck_list_chunks = [deck_list[i: i+2] for i in range(0, len(deck_list), 2)]
    return render(request, "flashcards/deck_list.html", {"deck_list_chunks": deck_list_chunks})


def card_test(request, id):
    return render(request, "flashcards/card_test.html", {'form': TestCardForm()})

