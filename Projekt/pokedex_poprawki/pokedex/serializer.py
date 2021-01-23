from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['pok_id', 'pok_nazwa', 'pok_waga', 'pok_wzrost', 'plec', 'trener', 'wersja_gry', 'typ']


class TrenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trener
        fields = ['trener_id', 'imie', 'nazwisko', 'plec', 'data_urodzenia', 'wersja_gry']


class PodstawoweStatySerializer(serializers.ModelSerializer):
    class Meta:
        model = PodstawoweStaty
        fields = ['idstatystyki', 'pod_hp', 'pod_atk', 'pod_def', 'pod_sp_atk', 'pod_sp_def', 'pod_speed', 'pokemon']


class RuchySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruchy
        fields = ['ruch_id', 'ruch_nazwa', 'ruch_sila', 'ruch_koszt', 'ruch_celnosc', 'pokemon', 'typ']


class TypySerializer(serializers.ModelSerializer):
    class Meta:
        model = Typy
        fields = ['typ_id', 'typ_nazwa']


class WersjaGrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WersjaGry
        fields = ['wersja_id', 'wersja_nazwa']
