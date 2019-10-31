import time
import sqlite3
import random
from bichinho import Bichinho, criarTamagushi
from caixaInput import main
import pygame 
from pygame.locals import *

lista = []
print(lista)
comprimento = 600
largura = 600
branca = (255,255,255)
preta = (0,0,0)
pygame.init()
tela   = pygame.display.set_mode((comprimento,largura))

pygame.display.set_caption('Tamagushi :)')

# definindo o tipo da fonte e seu tamanho
pygame.font.init()
font_p = pygame.font.get_default_font()
fonte_titulo = pygame.font.SysFont(font_p,45)
fonte_comando = pygame.font.SysFont(font_p,30)
comands = ('OPA, TDUBOM?', 'Atalhos para:', 'Criar um novo Bichinho -> B', 'Alimentar geral              -> U', 'Brincar com geral           -> D','exibir seu bichinho          -> A')
visivel = False
# MENU INICIAL: título, comandos
def menu():
    tela.fill(preta)
    x = 180
    y = 50
    titulo = fonte_titulo.render(comands[0], 1, branca)
    tela.blit(titulo, (x, y))
    if (visivel):
        if (len(lista)== 1):
             tela.blit(stitch,(200, 200))
        if (len(lista) == 2):
            tela.blit(stitch,(50, 200))
            pikachu = pygame.image.load(lista[1])
            tela.blit(pikachu,(350, 200))
    for i in range (5):
        if (i == 0):
            x= 40
            y = 90
        elif(i == 1):
            y = 110
            x = 60
        else:
            y += 20
        titulo = fonte_comando.render(comands[i+1], 1, branca)
        tela.blit(titulo, (x, y))

menu()

#comando
#for i in qtde de tamagushis:
#titulo = fonte_titulo.render('OPA, TDUBOM?', 1, branca)
  
ret = pygame.Rect(10,10,45,45)
# pygame.draw.rect(tela, (0,0,255), ret)

while True:
    
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_b:                
                    nomeecor = main()  
                    bichin = criarTamagushi(nomeecor[0],nomeecor[1])
                    lista.append(bichin.cor)
                    menu()
                if evento.key == pygame.K_a:
                    tela.fill(branca)
                    stitch = pygame.image.load(bichin.cor)
                    tela.blit(stitch,(200,200))
                    visivel = True
                if evento.key == pygame.K_RETURN:
                    menu()
#                if evento.key == pygame.K_0: 
        pygame.display.update()