time1 = input("Digite o nome do time: ")
gol1 = int(input("Digite quantos gols: "))
time2 = input("Digite o nome do time: ")
gol2 = int(input("Digite quantos gols: "))

if gol1 == gol2:
    print("O jogo deu EMPATE!")
elif gol1 < gol2:
    print("O time ", time2, "é o vencedor!")
else:
    print("O time ", time1, "é o vencedor!")
    