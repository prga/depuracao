def bubbleSort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

lista = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(lista)
print("A lista ordenada é: {}".format(lista))
