from django.db import models


class PodstawoweStaty(models.Model):
    idstatystyki = models.IntegerField()
    pod_hp = models.IntegerField()
    pod_atk = models.IntegerField()
    pod_def = models.IntegerField()
    pod_sp_atk = models.IntegerField()
    pod_sp_def = models.IntegerField()
    pod_speed = models.IntegerField()
    pokemon = models.ForeignKey('Pokemon', on_delete=models.CASCADE)


class Pokemon(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'meska'), (FEMALE, 'damska'))
    pok_id = models.IntegerField()
    pok_nazwa = models.CharField(max_length=45)
    pok_waga = models.IntegerField()
    pok_wzrost = models.IntegerField()
    plec = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    trener = models.ForeignKey('Trener', on_delete=models.CASCADE)
    wersja_gry = models.ForeignKey('WersjaGry', on_delete=models.CASCADE)
    typ = models.ForeignKey('Typy', on_delete=models.CASCADE)

    def __str__(self):
        return self.pok_nazwa


class Ruchy(models.Model):
    ruch_id = models.IntegerField()
    ruch_nazwa = models.CharField(max_length=45)
    ruch_sila = models.SmallIntegerField()
    ruch_koszt = models.SmallIntegerField()
    ruch_celnosc = models.SmallIntegerField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    typ = models.ForeignKey('Typy', on_delete=models.CASCADE)


class Trener(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'mezczyzna'), (FEMALE, 'kobieta'))
    trener_id = models.IntegerField()
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    plec = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    data_urodzenia = models.DateField()
    wersja_gry = models.ForeignKey('WersjaGry', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.imie


class Typy(models.Model):
    typ_id = models.IntegerField()
    typ_nazwa = models.CharField(max_length=45)

    def __str__(self):
        return self.typ_nazwa


class WersjaGry(models.Model):
    wersja_id = models.IntegerField()
    wersja_nazwa = models.CharField(max_length=45)

    def __str__(self):
        return self.wersja_nazwa
