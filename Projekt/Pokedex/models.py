from django.db import models

# Create your models here.

class pokemon(models.Model):
    pok_id = models.IntegerField(primary_key=True)
    pok_nazwa = models.CharField(max_length=45)
    pok_waga = models.IntegerField()
    pok_wzrost = models.IntegerField()
    trener_pokemony_idtrener_pokemony = models.ForeignKey('TrenerPokemony', on_delete=models.CASCADE)

    def __str__(self):
        return self.pok_nazwa

class TrenerPokemony(models.Model):
    idtrener_pokemony = models.IntegerField(primary_key=True)
    trener_trener = models.ForeignKey('Trener', on_delete=models.CASCADE)

class Trener(models.Model):
    trener_id = models.IntegerField(primary_key=True)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)

    def __str__(self):
        return self.imie
class podstawowe_staty(models.Model):
    pod_hp = models.IntegerField()
    pod_atk = models.IntegerField()
    pod_def = models.IntegerField()
    pod_sp_atk = models.IntegerField()
    pod_sp_def = models.IntegerField()
    pod_speed = models.IntegerField()
    pokemon_pok_id = models.OneToOneField('pokemon', on_delete=models.CASCADE, primary_key=True)

class wersja_gry(models.Model):
    wersja_id = models.IntegerField(primary_key=True)
    wersja_nazwa = models.CharField(max_length=45)
    pokemon_pok_id = models.ForeignKey('pokemon', on_delete=models.CASCADE)

    def __str__(self):
        return self.wersja_nazwa
class pokemon_ruchy(models.Model):
    idpokemon_ruchy = models.IntegerField(primary_key=True)
    pokemon_pok_id = models.ForeignKey('pokemon', on_delete=models.CASCADE)
    ruchy_ruch = models.ForeignKey('ruchy', on_delete=models.CASCADE)

class ruchy(models.Model):
    ruch_id = models.IntegerField(primary_key=True)
    ruch_nazwa = models.CharField(max_length=45)
    typy_typ_id = models.ForeignKey('typy',on_delete=models.CASCADE)
    ruch_sila = models.SmallIntegerField()
    ruch_koszt = models.SmallIntegerField()
    ruch_celnosc = models.SmallIntegerField()

class typy(models.Model):
    typ_id = models.IntegerField(primary_key=True)
    typ_nazwa = models.CharField(max_length=45)

    def __str__(self):
        return self.typ_nazwa
class pokemon_typy(models.Model):
    typy_typ_id = models.ForeignKey('typy', on_delete=models.CASCADE)
    pokemon_pok_id = models.OneToOneField('pokemon', on_delete=models.CASCADE)


