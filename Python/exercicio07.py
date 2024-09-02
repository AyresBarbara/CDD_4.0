# Receba 3 numeros e verifique se o aluno ta aprovado ou reprovado. Média igual a 7!#
nota1 = float(input("Informe sua nota 1: "))
nota2 = float(input("Informe sua nota 2: "))
nota3 = float(input("Informe sua nota 3: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print("Aluno Aprovado com média", media, "!")
else:
    if media >=4:
        print("Aluno em recuperação com média", media, "!")
    else:
        print("Aluno Reprovado com média", media, "!")
