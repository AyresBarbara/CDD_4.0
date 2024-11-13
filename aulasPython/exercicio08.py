# Receba 2 times e o numero de gols. Imprima quem venceu ou se deu empate
time1 = input("Digite o nome do time: ")
gol1 = int(input(f"Digite quantos gols o {time1} fez: "))
time2 = input("Digite o nome do time: ")
gol2 = int(input(f"Digite quantos gols o {time2} fez: "))

if gol1 == gol2:
    print("O jogo deu EMPATE!")
elif gol1 < gol2:
    print(f"O time {time2} é o vencedor!")
else:
    print(f"O time {time1} é o vencedor!")
