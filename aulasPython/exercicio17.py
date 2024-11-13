soma = 0
for n in range(1, 11, 1):
    num = int(input("Digite um número: "))
    if num % 2 == 1:
        soma = soma +num

print(soma)