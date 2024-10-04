usuario = [""]*5
senha = [""]*5

tam = len(usuario)

menu = 0
while menu != 4:
    menu = int(input("Digite a opção desejada: \n 1 - Cadastro \n 2 - Login \n 3 - Mostrar usuários \n 4 - Sair\nDigite sua opção:"))

    match menu:

        case 1:
            for x in range(tam):
                usuario[x] = input(f"Cadastre o nome do usuário [{x+1}]: ")
                senha[x] = input(f"Cadastre a senha do usuario [{x+1}]: ")
            print("Cadastro realizado com sucesso!")

        case 2:

            tent = 3
            while tent > 0:
                usuarioTent = input(f"Digite o nome do usuário: ")
                senhaTent = input(f"Digite a senha do usuário: ")
                login = False

                for x in range(tam):
                    if usuario[x] == usuarioTent and senha[x] == senhaTent:
                        print("Login efetuado com sucesso!")
                        login = True
                        break
                if login:
                    break
                else:
                    tent -= 1
                    print(f"Usuario ou senha incorretos. Verifique seua dados!\nVocê tem {tent} tentativas.\n")

            if tent <= 0:
                print("Conta bloqueada! \nVocê excedeu o número de tentativas, procure a sua agência. ")

        case 3:

            for x in range(tam):
                print(f"Nome do usuário: {usuario[x]} \nSenha: {senha[x]} \nPosição: {x+1}\n")

        case 4:
            print("Operação Encerrada!")
            break

        case _:
            print("Opção inválida! Tente novamente.")