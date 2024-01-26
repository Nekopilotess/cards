from django.urls import path, include
from . import views

app_name = 'cards'

urlpatterns = [
    path('', views.index, name='index'),
    path('cards/', views.cards, name='cards'),
    path('cards/<int:card_id>/', views.card, name='card'),
    path('cards/card_add', views.card_add, name='card_add'),
]
