import time
import sqlite3
import random
from db import Banco

banco = Banco()

class Bichinho():
    def __init__(self, nome, fome, tedio, idade, cor):
        self.nome  = nome
        self.fome  = fome
        self.tedio = tedio
        self.idade = idade
        self.cor = cor
    
    def altNome(self, nome):
        self.nome  = nome

    def alimentar(self, comida):
        self.fome  += comida
        if (self.fome > 100):
            self.fome = 100
            return self.fome
        else:
            return self.fome

    def brincar(self, tempo):
        self.tedio -= tempo
        if (self.tedio<0):
            self.tedio = 0
            return self.tedio
        else:
            return self.tedio 

    def altIdade(self, idade):
        self.idade = idade

    def seuTamagushi(self):
        return (self.nome, self.fome, self.tedio, self.idade, self.cor)

    def humor(self):
        humor = self.tedio - self.fome
        return humor

def criarTamagushi(nome, cor):    
    fome = random.randint(1,100)
    tedio = random.randint(1,100)    
    if (cor == 'azul'):
        cor = 'imagens/azul.png'
    elif (cor == 'azul1'):
        cor = 'imagens/azul1.png'
    elif (cor == 'amarelo'):
        cor = 'imagens/amarelo.png'
    elif (cor == 'vermelho'):
        cor = 'imagens/vermelho.png' 
    elif(cor == 'palhaço'):
        cor = 'imagens/palhaço.jpg'
    elif(cor == 'panda'):
        cor = 'imagens/panda.jpg'
    tamagushi = Bichinho(nome, fome, tedio, 0, cor)
#    banco.novoBichin(nome, fome, tedio, cor)
    return tamagushi

"""

x = criarTamagushi()

x.alimentar(10)
x.brincar(10)

print(x.seuTamagushi())



tamagushi = Bichinho(nome, 0, 10, 15, 3)
print(tamagushi.seuTamagushi())
ini = time.time()

print(type(tamagushi.seuTamagushi()))
print(tamagushi.humor())"""