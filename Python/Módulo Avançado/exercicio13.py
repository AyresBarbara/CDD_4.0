num = [""]*5
tam = len(num)
soma = 0
media = 0
maior = 0
menor = 1000000000
for x in range(tam):
    num[x] = int(input(f"Digite o {x+1}º numero: "))
    soma += num[x]

print("Números pares: ")
for x in range(tam):
    if num[x] %2 == 0:
        print(num[x], end= ", ")

for x in range(tam):
    if maior < num[x]:
        maior = num[x]
    if num[x]< menor:
        menor = num[x]
print(f"\nO maior valor é {maior} e o menor valor é {menor}")

"""maior = max(num)
menor = min(num)"""

media = soma/tam
print("Valores maiores que a média: ")
for x in range(tam):
    if num[x] > media:
        print(num[x], end= ", ")