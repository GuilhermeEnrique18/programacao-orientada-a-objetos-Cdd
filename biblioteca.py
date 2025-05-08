class Pessoa():
    def __init__(self, nome, idade, peso): # __init__ metodo construtor ou especial
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar(self):
        if self.comendo == True:
            print(f"{self.nome} não pode falar enquanto come.")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar enquanto dorme.")
        elif self.falando == True:
            print(f"{self.nome} já está falando.")
        else:
            self.falando = True
            print(f"{self.nome} começou a falar")

    def pararFalar(self):
        if self.falando == True:
            self.falando = False
            print(f"{self.nome} parou de falar.")
        else:
            print("Já está calado.")

    def comer(self):
        if self.falando == True:
            print(f"{self.nome} não pode comer enquanto fala.")
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer enquanto dorme.")
        elif self.comendo == True:
            print(f"{self.nome} já está comendo.")
        else:
            self.comendo = True
            print(f"{self.nome} esta comendo.")

    def pararComer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou de comer.")
        else:
            print("Não esta comendo nada.")

    def dormir(self):
        if self.falando == True:
            print(f"{self.nome} não pode dormir enquanto fala.")
        elif self.comer == True:
            print(f"{self.nome} não pode dormir enquanto come.")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo.")
        else:
            self.dormindo = True
            print(f"{self.nome} dormiuZZZzzzZZZzzz")

    def acordar(self):
        if self.dormindo == True:
            self.dormindo = False
            print(f"{self.nome} acordou.")
        else:
            print("Já está acordado")

class ContaBancaria():
    def __init__(self,numero,nome,tipo):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.saldo = 0
        self.limite = 0
        self.statusConta = False

    def depositar(self,deposito):
        self.saldo += deposito


    def exibirSaldo (self):
        print(self.saldo)

    def ativarConta(self):
        if self.statusConta:
            print("A sua conta já está ativa.")
        elif not self.statusConta: # é a  mesma coisa de " if self.statusConta == False: "
            self.statusConta = True

    def desativarConta(self):
        if self.saldo == 0:
            self.statusConta = False
            print("Conta desativada")
        else:
            print(f"Ainda resta um total de: {self.saldo} em sua conta, retire para desativar.")

    def sacar(self,valorSaque):
        self.saldo-=valorSaque
        print(f"Você sacou {valorSaque}")

        #fazer um método para definir um limite