from biblioteca import *
p1 = Pessoa ("João", 75, 21)


print(p1.nome, p1.peso, p1.idade)

if p1.falar() == True:
    print(p1.falar())
else:
    print(p1.falar)