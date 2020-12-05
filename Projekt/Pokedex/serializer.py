from rest_framework import serializers
from .models import *


class pokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = pokemon
        fields = ('pok_id', 'pok_nazwa', 'pok_waga', 'pok_wzrost', 'trener_pokemony_idtrener_pokemony')


class TrenerSerialize(serializers.ModelSerializer):
    class Meta:
        model = Trener
        fields = ('trener_id', 'imie', 'nazwisko')


class podSTSerialize(serializers.ModelSerializer):
    class Meta:
        model = podstawowe_staty
        fields = ('pod_hp', 'pod_atk', 'pod_def', 'pod_sp_atk', 'pod_sp_def', 'pod_speed', 'pokemon_pok_id')


class wersjaSerialize(serializers.ModelSerializer):
    class Meta:
        model = wersja_gry
        fields = ('wersja_id', 'wersja_nazwa', 'pokemon_pok_id')


class ruchSerialize(serializers.ModelSerializer):
    class Meta:
        model = ruchy
        fields = ('ruch_id', 'ruch_nazwa', 'ruch_sila', 'ruch_koszt', 'ruch_celnosc')


class typSerialize(serializers.ModelSerializer):
    class Meta:
        model = typy
        fields = ('typ_id', 'typ_nazwa')


class TrenerPokeSeria(serializers.ModelSerializer):
    class Meta:
        model = TrenerPokemony
        fields = ('idtrener_pokemony', 'trener_trener')
