from rest_framework import serializers
from .models import *


class pokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = pokemon
        fields = ('pok_id', 'pok_nazwa', 'pok_waga', 'pok_wzrost', 'trener_trener_id')


class podSTSerialize(serializers.ModelSerializer):
    class Meta:
        model = podstawowe_staty
        fields = ('pod_hp', 'pod_atk', 'pod_def', 'pod_sp_atk', 'pod_sp_def', 'pod_speed', 'pokemon_pok_id')


class wersjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = wersja_gry
        fields = ('wersja_id', 'wersja_nazwa', 'pokemon_pok_id')


class ruchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ruchy
        fields = ('ruch_id', 'ruch_nazwa', 'ruch_sila', 'ruch_koszt', 'ruch_celnosc')


class typSerializer(serializers.ModelSerializer):
    class Meta:
        model = typy
        fields = ('typ_id', 'typ_nazwa')


class trenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = trener
        fields = ('trener_id', 'imie', 'nazwisko')
