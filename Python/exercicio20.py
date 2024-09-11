num = int(input("Digite o número de aluno: "))
n = 0
soma = 0

while n < num:
    nota = float(input(f"Digite a nota do aluno {n}: "))
    n += 1
    soma += nota
media = soma / num
print(f"A média da turma é {media}")
