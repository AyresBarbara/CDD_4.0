hora1 = int(input("Digite a hora da primeira entrada: "))
min1 = int(input("Digite os minutos da primeira entrada: "))
hora2 = int(input("Digite a hora da segunda entrada: "))
min2 = int(input("Digite os minutos da segunda entrada: "))

if hora1 > 12:
    hora1 -= 12

if hora2 > 12:
    hora2 -= 12

totalH = hora1 + hora2
totalMin = min1 + min2

if totalMin >= 60:
    totalMin = totalMin - 60
    totalH = (totalH + 1)

if totalH >= 12:
    totalH -= 12

print(f"{totalH}:{totalMin}")
