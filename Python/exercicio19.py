soma = 0
x = 0

while x < 10:
    valor = float(input(f"Digite o valor {x}: "))
    x = x+1
    soma += valor
media = soma / x

print(f"A média dos valores é {media}")
