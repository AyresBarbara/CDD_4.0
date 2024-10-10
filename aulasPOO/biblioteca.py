class Pessoa:
    def __init__(self, nome, peso, idade, comendo = False, falando = False, dormindo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = falando
        self.comendo = comendo
        self.dormindo = dormindo

    def falar(self):
        print(f"{self.nome} está falando")
        self.falando == True

    def pararFalar(self):
        print(f"{self.nome} não está falando")
        self.falando == False

    def comer(self):
        print (f"{self.nome} foi comer")

    def pararComer(self):
        print()

    def acordar(self):
        print()

    def dormir(self):
        print(f"{self.nome} foi dormir")