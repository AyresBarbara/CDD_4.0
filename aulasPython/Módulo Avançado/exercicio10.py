num = [" "]*10
tam = len(num)
cont = 0

for x in range(tam):
    num[x] = int(input(f"Digite o {x+1}º número: "))

num2 = int(input(f"Digite um numero para pesquisar: "))
for x in range(tam):
    if num2 == num[x]:
       cont += 1
print(f"Os números são iguais, aparecendo {cont} vezes!")


