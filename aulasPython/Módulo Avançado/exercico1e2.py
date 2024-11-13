"""Criar um array tamanho 5 e preencher com
os nomes dos 5 alunos, informados pelo
usuário"""
nomes = ["", "", "", "", ""]
tam = len(nomes)

for x in range(tam):
    nomes[x] = input("Digite seu nome: ")

for x in range(tam):
    print(f"Nome: {nomes[x]}, na posição {[x]}")