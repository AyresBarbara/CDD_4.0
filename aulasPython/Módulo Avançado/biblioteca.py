#piramide 1\22\333
def piramide(n):
    for x in range(0, n+1):
        for y in range(x):
            print(x, end= " ")
        print()

#piramide 1\12\123
def piramide2(n):
    for x in range(1,n+1):
        for y in range(1, x+1):
            print(y, end= " ")
        print()

#Contar quantas vogais tem no texto
def lerVogais(frase):
    vogais =0
    for x in frase:
        if x in "aeiou":
            vogais +=1
    print(f"Tem {vogais} vogais")
