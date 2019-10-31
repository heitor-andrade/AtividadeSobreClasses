import time
import sqlite3
import random
from db import Banco
from bichinho import Bichinho, criarTamagushi
from caixaInput import main
import pygame 
from pygame.locals import *

comprimento = 600
largura = 600
 
branca = (255,255,255)
preta = (0,0,0)
pygame.init()
stitch = pygame.image.load('imagens/azul.png')
tela   = pygame.display.set_mode((comprimento,largura))

pygame.display.set_caption('Tamagushi :)')

# definindo o tipo da fonte e seu tamanho
pygame.font.init()
font_p = pygame.font.get_default_font()
fonte_titulo = pygame.font.SysFont(font_p,45)
fonte_comando = pygame.font.SysFont(font_p,30)

# MENU INICIAL: título, comandos
mensagens  ('')
def menu():
    tela.fill(preta)
    titulo = fonte_titulo.render('OPA, TDUBOM?', 1, branca)
    tela.blit(titulo, (180, 50))
    comando = fonte_comando.render('Atalhos para:', 1, branca)
    tela.blit(comando, (40,90))
    comando = fonte_comando.render('Criar um novo Bichinho -> 2', 1, branca)
    tela.blit(comando, (60,110))
    comando = fonte_comando.render('Alimentar geral -> 3', 1, branca)
    tela.blit(comando, (60,130))
    comando = fonte_comando.render('Brincar com geral -> 4', 1, branca)
    tela.blit(comando, (60,150))

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
            if evento.type == pygame.MOUSEBUTTONDOWN:
                tela.fill(branca)
                tela.blit(stitch,(200,300))
            if evento.type == 2:
                main()
                menu()

        pygame.display.update()