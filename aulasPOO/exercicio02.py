from bib02 import *

while True:
    opcao = int(input ("Escolha uma das opções do menu abaixo: \n 1 - gravar;\n 2 - ler;\n 3 - sair \n"))

    if (opcao == 1):
        texto = input("Digite seu texto:")
        gravar(texto)

    if(opcao == 2):
        ler()

    if(opcao == 3):
        print("Encerramos!")
        break