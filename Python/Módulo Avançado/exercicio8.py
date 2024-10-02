usuario = ["", "", "", "", ""]
senha = ["", "", "", "", ""]

for x in range(5):
    usuario[x] = input("Digite seu nome: ")
    senha[x] = input("Digite sua senha: ")

for x in range(5):
    print(f"Nome: {usuario[x]} com senha {senha[x]} na posição {[x]}")