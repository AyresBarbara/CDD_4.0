cont =0
while cont !=2:
    valor1 = int(input("Digite um valor: "))
    valor2 = int(input("Digite outro valor: "))
    while valor2 == 0:
        valor2 = int(input("Digite outro número, só aceitamos valores diferentes de 0: "))
    div = valor1 / valor2
    print(f"O resultado da divisaão é {div}.")

    cont = int(input("Você quer continuar? Digite 1 para continuar ou 2 para sair: "))
print("Divisão finalizada. Obrigado!")


