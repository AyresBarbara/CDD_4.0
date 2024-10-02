"""n = int(input("Digite um número: "))"""

def piramide(n):
    for x in range(0, n+1):
        for y in range(x):
            print(x, end= " ")
        print()

def piramide2(n):
    for x in range(1, n+1):
        for y in range(1, x+1):
            print(y, end= " ")
        print()

"""numero = int(input("Digite seu número: "))
piramide(numero)"""
