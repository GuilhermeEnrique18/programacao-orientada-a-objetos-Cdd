class Pessoa():
    def __init__(self, nome, idade, peso): # __init__ metodo construtor ou especial
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.falando = False
        self.comendo = False
        self.dormindo = False


    def falar(self):
            if self.falando == False:
                comendo = False
                dormindo = False
            print(f"{self.nome} começou a falar")

    def comer(self, comendo):
        print(f"{self.nome} está comendo: {comendo}")
        if self.comendo == False:


    def dormir(self):
        print(f"{self.nome} dormiuZZZzzzZZZzzz")
