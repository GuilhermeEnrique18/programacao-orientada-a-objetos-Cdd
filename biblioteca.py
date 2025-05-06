class Pessoa():
    def __init__(self, nome, idade, peso): # __init__ metodo construtor ou especial
        self.nome = nome
        self.idade = idade
        self.peso = peso
    def falar(self):
        print(f"{self.nome} começou a falar")
    def comer(self):
        print(f"{self.nome} está comendo")
    def dormir(self):
        print(f"{self.nome} dormiuZZZzzzZZZzzz")