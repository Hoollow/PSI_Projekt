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

from . import views
from django.urls import path, include

urlpatterns = \
    [
        path('pokemon', views.PokemonList.as_view(), name=views.PokemonList.name),
        path('pokemon/<int:pk>', views.PokemonDetail.as_view(), name=views.PokemonList.name),
        path('trener', views.TrenerList.as_view(), name=views.TrenerList.name),
        path('trener/<int:pk>', views.TrenerDetail.as_view(), name=views.TrenerList.name),
        path('wersjagry', views.WersjaGryList.as_view(), name=views.WersjaGryList.name),
        path('wersjagry/<int:pk>', views.WersjaGryDetail.as_view(), name=views.WersjaGryList.name),
        path('typy', views.TypyList.as_view(), name=views.TypyList.name),
        path('typy/<int:pk>', views.TypyDetail.as_view(), name=views.TypyList.name),
        path('ruchy', views.RuchyList.as_view(), name=views.RuchyList.name),
        path('ruchy/<int:pk>', views.RuchyDetail.as_view(), name=views.RuchyList.name),
        path('statystyki', views.PodstawoweStatyListy.as_view(), name=views.PodstawoweStatyListy.name),
        path('statystyki/<int:pk>', views.PodstawoweStatyDetail.as_view(), name=views.PodstawoweStatyListy.name),
        path('users/', views.UserList.as_view(), name=views.UserList.name),
        path('users/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
        path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)
    ]
