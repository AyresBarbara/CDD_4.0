# Digite um número e exiba. Ex.: 5 = 122333444455555
n = int(input("Digite um número: "))

for x in range(1, n+1):
    for y in range(x):
        print(x, end=" ")
    print() #pular linha
