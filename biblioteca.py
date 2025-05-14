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
        self.limite = 1000
        self.statusConta = False

    def depositar(self,deposito):
        if self.statusConta:
            self.saldo += deposito
        else:
            print("Conta desativada, antes de fazer o deposito, ative.")

    def exibirSaldo (self):
        print(f"Seu saldo atual é de: R${self.saldo} e você tem {self.limite} de limite.")

    def ativarConta(self):
        if self.statusConta:
            print("A sua conta já está ativa.")
        elif not self.statusConta: # é a  mesma coisa de " if self.statusConta == False: "
            self.statusConta = True
            print("Conta ativada!")

    def desativarConta(self):
        if self.saldo == 0:
            self.statusConta = False
            print("Conta desativada")
        elif self.saldo < 0:
            print(f"Impossivel desativar a conta. Você possui um saldo negativo com o banco de: {self.saldo}")
        else:
            print(f"Ainda resta um total de: {self.saldo} em sua conta, retire para desativar.")

    def sacar(self,valorSaque):
        if valorSaque <= self.saldo + self.limite:
            self.saldo -= valorSaque
            print(f"Você sacou R${valorSaque}. Saldo atual: R${self.saldo}")
        else:
            print(f"Saque não autorizado. Você excedeu o limite disponível de R${self.limite}.")

class Animal():
    def __init__(self,nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"O {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f"o {self.nome} está latindo...")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f"O {self.nome} MUUUUUUUUUUUUUU")

class Coelhinho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def guinchar(self):
        print(f"O {self.nome} foi guinchar ('iiii iiiiiiii')")

class Ingresso():
    def __init__(self,valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"O valor do ingresso é: {self.valor}")

class IngressoVip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
        self.valor *= 1.5
    def imprimeValor(self):
        print(f"Seu ingresso VIP é")

class Forma():
    def __init__(self ):
        self.perimetro = 0
        self.area = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaPerimetro(self, base,altura):
        self.perimetro = (base + altura) * 2
        print(f"O perimetro do retangulo é: {self.perimetro}")

    def calculaArea(self,base,altura):
        self.area = base*altura
        print(f"A area do retangulo {self.area}")

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaPerimetro(self, base,altura,lado):
        self.perimetro = base + altura + lado
        print(f"O perimetro do triangulo é: {self.perimetro}")

    def calculaArea(self,base,altura):
        self.area = (base*altura)/2
        print(f"A area do triangulo é: {self.area}")

class Atleta():
    def __init__(self):
        self.aposentado = False
        self.peso = 0
        self.aquecido = False

    def aposentar(self):
        self.aposentado = True

    def aquecer(self):
        if not self.aposentado:
            self.aquecido = True
            print("Aquecido")
        else:
            print("Ele está aposentado, não pode aquecer e praticar nada.")

class Corredor(Atleta):
    def __init__(self):
        super().__init__()

    def correr(self):
        if self.aquecido:
            print("Correndo")
        else:
            print("Precisa aquecer para correr")

class Nadador(Atleta):
    def __init__(self):
        super().__init__()

    def nadar(self):
        if self.aquecido:
            print("Nadando")
        else:
            print("Precisa aquecer para nadar")

class Ciclista(Atleta):
    def __init__(self):
        super().__init__()

    def pedalar(self):
        if self.aquecido:
            print("Pedalando")
        else:
            print("Precisa aquecer para pedalar")

class TriAtleta(Corredor,Nadador,Ciclista):
    def __init__(self):
        super().__init__()