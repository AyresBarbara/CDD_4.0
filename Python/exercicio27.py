n = int(input("Digite seu numero:"))

for x in range(0, n+1):
    for j in range(0, x+1):
        print(j, end=" ")
    print()