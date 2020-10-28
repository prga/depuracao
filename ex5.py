def maior_idade():
    idades = []
    for i in range(0,50):
        idades.append(int(input("Digite sua idade: ")))
    for i in range(0,5):
        if idades[i] > 18:
            print(idades[i])

maior_idade()