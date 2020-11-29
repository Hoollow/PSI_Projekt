from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class PodstawoweStaty(models.Model):
    pod_hp = models.IntegerField(blank=True, null=True)
    pod_atk = models.IntegerField(blank=True, null=True)
    pod_def = models.IntegerField(blank=True, null=True)
    pod_sp_atk = models.IntegerField(blank=True, null=True)
    pod_sp_def = models.IntegerField(blank=True, null=True)
    pod_speed = models.IntegerField(blank=True, null=True)
    pokemon_pok = models.OneToOneField('Pokemon', models.DO_NOTHING, primary_key=True)

    class Meta:

        db_table = 'podstawowe_staty'


class Pokemon(models.Model):
    pok_id = models.IntegerField(primary_key=True)
    pok_nazwa = models.CharField(max_length=45)
    pok_waga = models.IntegerField(blank=True, null=True)
    pok_wzrost = models.IntegerField(blank=True, null=True)
    trener_pokemony_idtrener_pokemony = models.ForeignKey('TrenerPokemony', models.DO_NOTHING, db_column='Trener_pokemony_idTrener_pokemony')  # Field name made lowercase.

    class Meta:
        db_table = 'pokemon'
        unique_together = (('pok_id', 'trener_pokemony_idtrener_pokemony'),)


class PokemonRuchy(models.Model):
    idpokemon_ruchy = models.IntegerField(primary_key=True)
    pokemon_pok = models.ForeignKey(Pokemon, models.DO_NOTHING)
    ruchy_ruch = models.ForeignKey('Ruchy', models.DO_NOTHING)

    class Meta:
        db_table = 'pokemon_ruchy'
        unique_together = (('idpokemon_ruchy', 'pokemon_pok', 'ruchy_ruch'),)


class PokemonTypy(models.Model):
    typy_typ = models.ForeignKey('Typy', models.DO_NOTHING)
    pokemon_pok = models.OneToOneField(Pokemon, models.DO_NOTHING, primary_key=True)

    class Meta:
        db_table = 'pokemon_typy'


class PokemonUmiejetnosci(models.Model):
    umiejetnosci_umi = models.ForeignKey('Umiejetnosci', models.DO_NOTHING)
    pokemon_pok = models.OneToOneField(Pokemon, models.DO_NOTHING, primary_key=True)

    class Meta:
        db_table = 'pokemon_umiejetnosci'


class Ruchy(models.Model):
    ruch_id = models.IntegerField(primary_key=True)
    ruch_nazwa = models.CharField(max_length=45)
    typy_typ = models.ForeignKey('Typy', models.DO_NOTHING)
    ruch_sila = models.SmallIntegerField(blank=True, null=True)
    ruch_koszt = models.SmallIntegerField(blank=True, null=True)
    ruch_celnosc = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ruchy'


class Trener(models.Model):
    trener_id = models.IntegerField(primary_key=True)
    imie = models.CharField(db_column='Imie', max_length=45)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'trener'


class TrenerPokemony(models.Model):
    idtrener_pokemony = models.IntegerField(db_column='idTrener_pokemony', primary_key=True)  # Field name made lowercase.
    trener_trener = models.ForeignKey(Trener, models.DO_NOTHING, db_column='Trener_trener_id')  # Field name made lowercase.

    class Meta:
        db_table = 'trener_pokemony'


class Typy(models.Model):
    typ_id = models.IntegerField(primary_key=True)
    typ_nazwa = models.CharField(max_length=45)

    class Meta:
        db_table = 'typy'


class Umiejetnosci(models.Model):
    umi_id = models.IntegerField(primary_key=True)
    umi_nazwa = models.CharField(max_length=45)

    class Meta:
        db_table = 'umiejetnosci'


class WersjaGry(models.Model):
    wersja_id = models.IntegerField(primary_key=True)
    wersja_nazwa = models.CharField(max_length=45)
    pokemon_pok = models.ForeignKey(Pokemon, models.DO_NOTHING)

    class Meta:

        db_table = 'wersja_gry'
        unique_together = (('wersja_id', 'pokemon_pok'),)


