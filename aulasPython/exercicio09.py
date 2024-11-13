combustivel = input("Informe o tipo de combustivel que voce quer abastecer, E - Etanol ou G - Gasolina:")
litros = float(input(f"Digite quantos litros de {combustivel} voce quer abastecer: "))

if combustivel == 'G':
    custo = (litros * 5.80)
    print(f"O valor a ser pago é {custo}")
else:
    custo = (litros * 4.90)
    print(f"O valor a ser pago é {custo}")
