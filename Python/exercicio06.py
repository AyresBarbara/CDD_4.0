num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro numero: "))

if num1 == num2:
    print("Os números digitados são iguais!")
else:
    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)