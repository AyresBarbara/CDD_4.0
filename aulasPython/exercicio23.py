neg = 0
cont =0
while cont != 2:
    for x in range(10):
        valor = int(input("Digite o valor:"))
        if valor < 0:
            neg +=1

    print(f"Tem {neg} valores negativos")
    cont = int(input("Deseja continuar? Digite 1 para continuar ou 2 para sair: "))
print("Sistema encerrado!")