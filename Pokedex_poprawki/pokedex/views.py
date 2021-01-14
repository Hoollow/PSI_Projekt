# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from django.contrib.auth.models import User
from pokedex.serializer import *
from pokedex.models import *



class PokemonList(generics.ListCreateAPIView):
    queryset = pokemon.objects.all()
    serializer_class = pokemonSerializer
    search_fields = ['pok_id', 'pok_nazwa']
    filterset_fields = ['pok_nazwa']
    ordering_fields = ['pok_nazwa'] #sortowanie nazwy od najw lub namniejszej
class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = pokemon.objects.all()
    serializer_class = pokemonSerializer

class TrenerList(generics.ListCreateAPIView):
    queryset = trener.objects.all()
    serializer_class = trenerSerializer

class TrenerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = trener.objects.all()
    serializer_class = trenerSerializer

class PodStatyList(generics.ListCreateAPIView):
    queryset = podstawowe_staty.objects.all()
    serializer_class = podSTSerialize

class PodStatyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = podstawowe_staty.objects.all()
    serializer_class = podSTSerialize


class WersjaGryLIst(generics.ListCreateAPIView):
    queryset = wersja_gry.objects.all()
    serializer_class = wersjaSerializer

class WersjaGryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = wersja_gry.objects.all()
    serializer_class = wersjaSerializer


class RuchyList(generics.ListCreateAPIView):
    queryset = ruchy.objects.all()
    serializer_class = ruchSerializer

class RuchyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ruchy.objects.all()
    serializer_class = ruchSerializer

class TypyList(generics.ListCreateAPIView):
    queryset = typy.objects.all()
    serializer_class = typSerializer

class TypyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = typy.objects.all()
    serializer_class = typSerializer