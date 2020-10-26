lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
liczba_liter1 = lorem.count("z")
liczba_liter2 = lorem.count("a")
print(f"W tekście jest {liczba_liter1} liter z oraz {liczba_liter2} a")
imie = "Marcin"
nazwisko = "Krzemiński"
litera_1 = imie[2]
litera_2 = nazwisko[3]
liczba_liter1 = lorem.count(litera_1)
liczba_liter2 = lorem.count(litera_2)
print(f"W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}")
print(dir('WOLOLO'))
help('WOLOLO'.lower())
print(f'{imie[:: -1]} {nazwisko[::-1]}')
lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = lista[5:]
lista1 = lista[:5]
print(lista1)
print(lista2)
lista = [0]
lista.extend(lista1)
lista.extend(lista2)
print(lista)
lista.sort(reverse=True)
print(lista)
student1 = "marcin","krzem", 3123123
student2 = "aligner","nazwisko", 4847393
print(student1)
# tworzenie słownika
slownik = {}
slownik1 = {'numer_indeksu': 150990, 'imie': 'Marcin', 'nazwisko':'Krzemiński', 'wiek':23, 'rok_urodzenia': '23 września1997', 'email': 'yoru1997@gmail.com', 'adres': 'Paderewskiego 13'}
var = slownik1['imie']
var2 = slownik1['email']
print(var)
print(var2)
listatel = [5,5,5,5,4,34,3,5,34,534,5345,346,35324,42,4,54]
print(listatel)
telefony=set(listatel)
print(telefony)
#zad 11
x = range(1, 10)
for n in x:
  print(n)
#zad 12
x = range(100, 20, -5)
for n in x:
  print(n)
  slownika = {
      "brand": "Daewoo",
      "model": "tico",
      "rok": "1996"
  }
  slownikb = {
      "imie": "Marcin",
      "nazwisko": "Krzemiński",
      "indeks": "484833"
  }
  lista = [slownika, slownikb]
  print("student " + lista[1].get("imie") + " " + lista[1].get("nazwisko") + " z indeksem numer " + lista[1].get(
      "indeks") + " jechal swoim " + lista[0].get("model") + " " + lista[0].get("brand") + " z roku " + lista[0].get(
      "rok"))