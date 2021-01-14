"""Projekt_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from pokedex import views
from django.urls import path, include

urlpatterns = \
    [
        path('pokemon', views.PokemonList.as_view()),
        path('pokemon/<int:pk>', views.PokemonDetail.as_view()),
        path('trener', views.TrenerList.as_view()),
        path('trener/<int:pk>', views.TrenerDetail.as_view()),
        path('podstawowe-staty', views.PodStatyList.as_view()),
        path('podstawowe-staty/<int:pk>', views.PodStatyDetail.as_view()),
        path('wersja_gry', views.WersjaGryLIst.as_view()),
        path('wersja_gry/<int:pk>', views.WersjaGryDetail.as_view()),
        path('pokemon_ruchy', views.RuchyList.as_view()),
        path('pokemon_ruchy/<int:pk>', views.RuchyDetail.as_view()),
        path('typy', views.TypyList.as_view()),
        path('typy/<int:pk>', views.TypyDetail.as_view()),

    ]
