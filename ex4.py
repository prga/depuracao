def media_100():
    media = 0
    for i in range(0, 10):
        numero = float(input("Digite um número: "))
        media = numero + numero/10
    print("A média é {}".format(media))

media_100()