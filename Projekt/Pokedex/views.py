# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets, generics, status
from pokedex.serializer import *
from pokedex.forms import *


def myView(request):
    return HttpResponse('Hello, World!')


class PokemonView(viewsets.ModelViewSet):
    queryset = pokemon.objects.all()
    serializer_class = pokemonSerializer

class TrenerView(viewsets.ModelViewSet):
    queryset = Trener.objects.all()
    serializer_class = TrenerSerialize


class TrenerPokView(viewsets.ModelViewSet):
    queryset = TrenerPokemony.objects.all()
    serializer_class = TrenerPokeSeria
