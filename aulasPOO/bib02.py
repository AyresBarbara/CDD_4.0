
def gravar(texto):
    with open("registro.txt", "a") as arquivo:
        arquivo.write(f'{texto}\n')

def ler():
    with open("registro.txt", "r") as arquivo2:
        txt = arquivo2.read()
        print(txt)