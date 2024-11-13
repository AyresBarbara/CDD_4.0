#Receba um número e mostre todos os impares
num = int(input("Digite um número: "))

for i in range(1, num+1, 1):
    if i % 2 == 1:
        print(i)
