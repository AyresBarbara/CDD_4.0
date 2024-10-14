class Pessoa:
    def __init__(self, nome, peso, idade, comendo = False, falando = False, dormindo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = falando
        self.comendo = comendo
        self.dormindo = dormindo

    def falar(self):
        if self.falando == False: #Se ele não tiver calado
            print(f"{self.nome} está falando")
            self.falando = True
        else:
            print(f"{self.nome} já está falando")

    def pararFalar(self):
        print(f"{self.nome} parou de falar")
        self.falando = False

    def comer(self):
        if self.comendo == False:
            print (f"{self.nome} está comendo")
            self.comendo = True
        else:
            print(f"{self.nome} já está comendo")

    def pararComer(self):
        print(f"{self.nome} parou de comer")
        self.comendo = False

    def acordar(self):
        print(f"{self.nome} não está dormindo")
        self.dormindo = False

    def dormir(self):
        if self.dormindo == False:
            print(f"{self.nome} foi dormir")
            self.dormindo = True
        else:
            print(f"{self.nome} já foi dormir")