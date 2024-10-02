usuario = ["", "", "", "", ""]
senha = ["", "", "", "", ""]

tam = len(usuario)

for x in range(tam):
    usuario[x] = input("Digite seu nome: ")
    senha[x] = input("Digite sua senha: ")

for x in range(tam):
    print(f"Nome: {usuario[x]} com senha {senha[x]} na posição {[x]}")