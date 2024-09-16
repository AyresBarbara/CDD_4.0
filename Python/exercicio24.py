pin = 1234
senha = int(input("Digite sua senha: "))
cont = 1

while senha != pin and cont < 3:
    senha = int(input(f"Senha incorreta\n"
                      f"VocÊ tem {3-cont} tentativas"
                      f"Digite sua senha: "))
    cont +=1
if cont == 3:
    print("Senha bloqueada")
else:
    print("Login liberado com sucesso!")
