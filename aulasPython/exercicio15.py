#Ler um número inteiro e mostrar a tabuada de multiplicação (1-10)
num = int(input("Digite o número que você deseja a tabuada: "))
tab = 0
for i in range(1, 11, 1):
    tab = num * i
    print(f"{num} x {i} = {tab}")
