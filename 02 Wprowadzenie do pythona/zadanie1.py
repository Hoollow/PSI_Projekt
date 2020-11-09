def listy(a_lista, b_lista):
    a_lista = list(a_lista)
    b_lista = list(b_lista)
    c_lista = []
    for i in range(len(a_lista)):
        if a_lista[i] % 2 == 0:
            c_lista.append(a_lista[i])
    for j in range(len(b_lista)):
        if b_lista[j] % 2 == 1:
            c_lista.append(b_lista[j])
    return c_lista


x = listy(a_lista=[1, 2, 3, 4, 5, 3], b_lista=[2, 2, 3, 4, 5, 6])
print(x)