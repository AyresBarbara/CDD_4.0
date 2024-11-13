# Ler o número existente de alunos, ler as notas, calcular e escrever a média aritmetica
numAl = int(input("Digite a quantidade de alunos: "))
soma = 0

for x in range(1, numAl + 1):
    nota = float(input(f"Digite a nota do aluno {x}: "))
    soma += nota

media = soma / numAl

print(f"A média dos alunos é {media: .2f}")
