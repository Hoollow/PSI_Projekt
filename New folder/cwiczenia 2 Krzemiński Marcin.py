# Zadanie 1
def listy(a_lista, b_lista):
    a_lista=list(a_lista)
    b_lista=list(b_lista)
    c_lista=[]
    for i in range(len(a_lista)):
        if a_lista[i] % 2 == 0:
            c_lista.append(a_lista[i])
    for j in range(len(b_lista)):
        if b_lista[j] % 2 == 1:
            c_lista.append(b_lista[j])
    return c_lista

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [20, 19, 18, 17, 16, 15]

print(listy(lista1, lista2))

# Zadanie 2
def slownik(data_text):
    slownik = {}
    lista = list(data_text)
    slownik = dict([("length", len(data_text)), ("letters", lista), ("big_letters", data_text.upper()), ("small_letters", data_text.lower())])
    return slownik

print(slownik('pies'))

# Zadanie 3

def usuwanie(text, letter):
    print (text)
    text1 = list(text)
    text2 = []
    for i in range(len(text)):
        if text1[i] != letter:
            text2.append(text1[i])
    text3 = ''.join([str(elem) for elem in text2])

    return text3
print(usuwanie('pies','s'))

# Zadanie 4

def przeliczka(cel):
    print("Celcjusz: ",cel)
    print("Fahrenheit: ",cel*1.8 + 32)
    print("Kelvin: ",cel + 273.15)
    print("Rankine: ",(cel + 273.15)*1.8)

przeliczka(30)

class Calculator:
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

dzialanie = Calculator(5, 6)

print(dzialanie.add())
print(dzialanie.difference())
print(dzialanie.multiply())
print(dzialanie.divide())

#Zadanie6
class ScenceCalculator(Calculator):
    def exponentiation(self):
        return pow(self.a, self.b)

potegowanie = ScenceCalculator(2, 1)
print(potegowanie.exponentiation())

#zadanie 7

def od_tylu(text):
    print(f'{text[::-1]}')

od_tylu("koteł")

#Zadanie9
import file_menager as menagoplikow

k = menagoplikow.FileMenager("notatka.txt")

k.read_file("notatka.txt")
k.update_file("Zabrze")
