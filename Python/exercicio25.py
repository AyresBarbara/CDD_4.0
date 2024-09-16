nota1 = float(input("Digite a nota da 1a Av.(0-10): "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida!")
    nota1 = float(input("Digite a nota da 1a Av.(0-10): "))

nota2 = float(input("Digite a nota da 2a Av.(0-10): "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida!")
    nota2 = float(input("Digite a nota da 2a Av.(0-10): "))

soma = nota1 + nota2
media = soma / 2

print(f"A média do aluno é {media}")