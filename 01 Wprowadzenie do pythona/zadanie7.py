lista = [1,2,3,4,5,6,7,8,9,10]
lista1 = lista[:len(lista)//2]
lista2 = lista[len(lista)//2:]
print(lista1)
print(lista2)
lista3 = lista1 + lista2
lista4 = [0]
lista4.extend(lista1)
lista4.extend(lista2)
print(lista4)
print("Oryginalna lista: ", lista4)
lista4.reverse()
print("Odwrócona lista: ", lista4)
