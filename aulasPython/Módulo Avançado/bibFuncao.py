def somar(*numeros):
    t = len(numeros)
    soma = 0
    for x in range(t):
        soma += numeros[x]
    print(soma)
