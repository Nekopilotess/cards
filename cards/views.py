from django.shortcuts import render, redirect

from .models import Card
from .forms import CardForm


def index(request):
    return render(request, 'cards/index.html')

def cards(request):
    cards = Card.objects.all()
    context = {'cards': cards}
    return render(request, 'cards/cards.html', context)


def card(request, card_id):
    card = Card.objects.get(id=card_id)
    context = {'card': card}
    return render(request, 'cards/card.html', context)

def card_add(request):
    if request.method != 'POST':
        form = CardForm()
    else:
        form = CardForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards:cards')

    context = {'form': form}
    return render(request, 'cards/card_add.html', context)
