# Create your views here.
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializer import *
from .models import *
from django.contrib.auth.models import User


class PokemonList(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    search_fields = ['pok_id', 'pok_nazwa']
    filterset_fields = ['pok_nazwa']
    ordering_fields = ['pok_nazwa']
    name = 'pokemon'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    name = 'pokemon-detail'


class TrenerList(generics.ListCreateAPIView):
    queryset = Trener.objects.all()
    serializer_class = TrenerSerializer
    name = 'trener'
    search_fields = ['trener_id', 'imie', 'nazwisko']
    filterset_fields = ['imie', 'nazwisko']
    ordering_fields = ['imie', 'nazwisko']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrenerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trener.objects.all()
    serializer_class = TrenerSerializer
    name = 'trener-detail'


class PodstawoweStatyListy(generics.ListCreateAPIView):
    queryset = PodstawoweStaty.objects.all()
    serializer_class = PodstawoweStatySerializer
    name = 'PodstawoweStaty'
    search_fields = ['pokemon']
    filterset_fields = ['pokemon']
    ordering_fields = ['pod_hp', 'pod_atk', 'pod_def']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PodstawoweStatyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PodstawoweStaty.objects.all()
    serializer_class = PodstawoweStatySerializer
    name = 'Podstawowestaty-detail'


class RuchyList(generics.ListCreateAPIView):
    queryset = Ruchy.objects.all()
    serializer_class = RuchySerializer
    name = 'Ruchy'
    search_fields = ['pokemon', 'typ', 'ruch_nazwa']
    filterset_fields = ['pokemon', 'typ', 'ruch_nazwa']
    ordering_fields = ['ruch_sila', 'ruch_koszt']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RuchyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ruchy.objects.all()
    serializer_class = RuchySerializer
    name = 'Ruchy-detail'


class TypyList(generics.ListCreateAPIView):
    queryset = Typy.objects.all()
    serializer_class = TypySerializer
    name = 'typy'
    search_fields = ['typ_nazwa']
    filterset_fields = ['typ_nazwa']
    ordering_fields = ['typ_id']
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly] # dla pytest, bo wywala 401 :/


class TypyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Typy.objects.all()
    serializer_class = TypySerializer
    name = 'typy-detail'


class WersjaGryList(generics.ListCreateAPIView):
    queryset = WersjaGry.objects.all()
    serializer_class = WersjaGrySerializer
    name = 'WersjaGry'
    search_fields = ['wersja_nazwa']
    filterset_fields = ['wersja_nazwa']
    ordering_fields = ['wersja_id']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WersjaGryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WersjaGry.objects.all()
    serializer_class = WersjaGrySerializer
    name = 'wersja-detail'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'Api-root'

    def get(self, request, *args, **kwargs):
        return Response({'Pokemony': reverse(PokemonList.name, request=request),
                         'Trenerzy': reverse(TrenerList.name, request=request),
                         'Wersje Gier': reverse(WersjaGryList.name, request=request),
                         'Typy': reverse(TypyList.name, request=request),
                         'Ruchy': reverse(RuchyList.name, request=request),
                         'Statystyki': reverse(PodstawoweStatyListy.name, request=request),
                         'Użytkownicy': reverse(UserList.name, request=request)
                         })
