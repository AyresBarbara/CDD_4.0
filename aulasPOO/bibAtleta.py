class Atleta:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.aposentado = False
        self.aquecido = False

    def aposentar(self):
        print(f"O atleta {self.nome} está aposentado")
        self.aposentado == True

    def desaposentar(self):
        print(f"O atleta {self.nome} não está aposentado")
        self.aposentado == False

    def aquecer(self):
        print(f"O atleta {self.nome} está aquecido!")
        self.aquecido == True

class Corredor(Atleta):

    def __init__(self,nome, peso):
        super().__init__(nome, peso)

    def correr(self):
        if self.aposentado == False:
            if self.aquecido == True:
                print(f"O atleta {self.nome} pode correr")
            else:
                print(f"O atleta não pode correr pq não está aquecido")
        else:
            print("O atleta não pode correr pq está aposentado")