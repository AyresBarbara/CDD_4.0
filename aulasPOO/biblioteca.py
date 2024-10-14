class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar(self):
        if self.falando == False: #Se ele não tiver calado
            if self.comendo == False:
                if self.dormindo == False:
                    print(f"{self.nome} está falando")
                    self.falando = True
                else:
                    print(f"{self.nome} não pode falar pq ele está dormindo")
            else:
                print(f"{self.nome} não pode falar pq ele está comendo")
        else:
            print(f"{self.nome} já está falando")

    def pararFalar(self):
        if self.falando == True:
            print(f"{self.nome} parou de falar")
            self.falando = False

    def comer(self):
        if self.comendo == False:
            if self.falando == False:
                if self.dormindo == False:
                    print (f"{self.nome} está comendo")
                    self.comendo = True
                else:
                    print(f"{self.nome} já está dormindo, não pode comer agora")
            else:
                print(f"{self.nome} está falando, não pode comer agora")
        else:
            print(f"{self.nome} já está comendo")

    def pararComer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer")
            self.comendo = False

    def dormir(self):
        if self.dormindo == False:
            if self.comendo == False:
                if self.falando == False:
                    print(f"{self.nome} foi dormir")
                    self.dormindo = True
                else:
                    print(f"{self.nome} está falando, não pode dormir agora")
            else:
                print(f"{self.nome} está comendo, não pode dormir agora")
        else:
            print(f"{self.nome} já foi dormir")

    def acordar(self):
        if self.dormindo == True:
            print(f"{self.nome} não está dormindo")
            self.dormindo = False

class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.comendo = False
    def comer(self):
        if self.comendo == False:
            print(f"{self.nome} está comendo!")
            self.comendo = True

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} está miando")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"{self.nome} está mugindo!")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"{self.nome} está latindo!")