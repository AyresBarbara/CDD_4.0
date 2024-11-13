usuario = [""]*5
senha = [""]*5

tam = len(usuario)

menu = 0
while menu != 4:
    menu = int(input("Digite a opção desejada: \n 1 - Cadastro \n 2 - Login \n 3 - Mostrar usuários \n 4 - Sair\nDigite sua opção:"))
    print()

    match menu:

        case 1:
            for x in range(tam):
                while True:
                    user = input(f"Cadastre o nome do usuário [{x+1}]: ")
                    if user.strip() == "":
                        print("Usuário inválido! Adicione um nome válido!")
                        continue
                    if user in usuario:
                        print("Usuário já cadastrado. Tente outro nome!\n")
                        continue

                    password = input(f"Cadastre a senha do usuario [{x+1}]: ")
                    if password in senha:
                        print("Senha já cadastrado. Tente outra senha!\n")
                        continue
                    if password.strip() == "":
                        print("Senha inválido! Adicione uma senha válida!")
                        continue

                    usuario[x] = user
                    senha[x] = password
                    break
            print("Cadastro realizado com sucesso!\n")
        case 2:

            tent = 3
            while tent > 0:
                usuarioTent = input(f"Digite o nome do usuário: ").strip()
                senhaTent = input(f"Digite a senha do usuário: ").strip()
                login = False

                for x in range(tam):
                    if usuario[x] == usuarioTent and senha[x] == senhaTent:
                        print("Login efetuado com sucesso!\n")
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
            print("Usuários Cadastrados: ")
            for x in range(tam):
                if usuario[x] and senha[x]:
                    print(f"Nome do usuário: {usuario[x]} \nSenha: {senha[x]} \nPosição: {x+1}\n")

        case 4:
            print("Operação Encerrada!")
            break

        case _:
            print("Opção inválida! Tente novamente.\n")