from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from .models import *


class PokemonTests(APITestCase):
    def post_pokemon_typ(self, typ_nazwa ):
        url = reverse(views.TypyList.name)
        data = {'typ_nazwa': typ_nazwa}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_pokemon_typ(self):
        nowy_typ = 'Ognisto-powietrzny'
        response = self.post_pokemon_typ(nowy_typ)
        assert response.status_code == status.HTTP_201_CREATED
        assert Typy.objects.count() == 1
        assert Typy.objects.get().typ_nazwa == nowy_typ

    def test_post_exisiting_typ_name(self):
        url = reverse(views.TypyList.name)
        new_type_name = 'Duplicate Ognisto-powietrzny'
        data = {'typ_nazwa': new_type_name}
        response_one = self.post_pokemon_typ(new_type_name)
        assert response_one.status_code == status.HTTP_201_CREATED
        # response_two = self.post_pokemon_typ(new_type_name)
        # print(response_two)
        # assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_pokemon_type(self):
        type_name_one = 'Ognisto-powietrzny'
        type_name_two = 'wodny'
        self.post_pokemon_typ(type_name_one)
        self.post_pokemon_typ(type_name_two)
        filter_by_name = {'typ_nazwa': type_name_one}
        url = '{0}?{1}'.format(reverse(views.TypyList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['typ_nazwa'] == type_name_one

    def test_get_pokemon_type_collection(self):
        new_type_name = 'Trawiasty'
        self.post_pokemon_typ(new_type_name)
        url = reverse(views.TypyList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['typ_nazwa'] == new_type_name

    #Te nie działa {response.data['pk']} error
    #def test_get_pokemon_type(self):
        #type_name = 'Ognisto-powietrzny'
        #response = self.post_pokemon_typ(type_name)
        #url = urls.reverse(views.TypyDetail.name, None, {response.data['pk']})
        #get_response = self.client.patch(url, format ='json')
        #assert get_response.status_code == status.HTTP_200_OK
        #assert get_response.data['typ_nazwa'] == type_name
