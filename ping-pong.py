import pygame, random
from pygame.locals import *

# Tamanho de cada bloco
tamanho = 10
joga_sozinho = True
max_tentativas = 5 

def posicao_bola():
    """
    Gera uma posição aleatória para a bola
    """
    return (random.randrange(0, (600 - tamanho), tamanho), 0)

def auto_play(ligado = False):
    """Algoritmo para jogar sozinho"""
    if ligado:    
         distancia = bola[0] - raquete[4][0]     
         if distancia > 0:
             direcao = DIREITA
         else:
             direcao = ESQUERDA
    return direcao

# Cria as variáveis
ESQUERDA = 'ESQUERDA'
DIREITA = 'DIREITA'
BAIXO = 'BAIXO'
CIMA = 'CIMA'


# Cria a tela
pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Ping-Pong')

# Cria a raquete
raquete = []
for i in range(9):
    raquete.append((i * tamanho, 600 - tamanho))

textura_raquete = pygame.Surface((tamanho, tamanho))
textura_raquete.fill((255, 255, 255))

# Cria a bola
bola = posicao_bola()
textura_bola = pygame.Surface((tamanho, tamanho))
textura_bola.fill((255, 255, 255))
direcao_x_bola = ESQUERDA
direcao_y_bola = BAIXO

# Define algumas vaiaveis que serão usadas no loop
direcao = ESQUERDA
pontos = 0
tentativas = 1

relogio = pygame.time.Clock()

# Cria e mostra um texto na tela
pygame.font.init()
fonte_padrao = pygame.font.get_default_font()
fonte = pygame.font.SysFont(fonte_padrao, 60)
    
for i in range(3, -1, -1):
    tela.fill((0, 0, 0))
    texto = fonte.render(f'O jogo começa em {i}...', 1, (255, 255, 255))
    tela.blit(texto, (80,270))
    pygame.time.delay(1000)
    pygame.display.update()

while True:
    
    # Atualiza a tela a cada tempo (milisegundos)
    relogio.tick(30)    
    # Limpa a tela
    tela.fill((0, 0, 0))
    
    # Coloca a bola na tela    
    tela.blit(textura_bola, bola)
    
    # Coloca A raquete na tela
    for pos in raquete:
        tela.blit(textura_raquete, pos)

    # Mostra a contagem de pontos
    texto = fonte.render(f'Pontos: {pontos}, Tentativas: {tentativas}', 1, (255, 255, 255))
    tela.blit(texto, (0, 0))
        
    # Administra os eventos
    for event in pygame.event.get():
        # Fechar a janela
        if event.type == QUIT:
            pygame.quit()
        
        # Andar para esquerda ou direita
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                direcao = ESQUERDA
            if event.key == K_RIGHT:
                direcao = DIREITA
                
    direcao = auto_play(joga_sozinho) if joga_sozinho else None
        
    # Cria o movimento da bola
    if direcao_y_bola == BAIXO:
            if bola[1] < (600 - tamanho):
                bola = (bola[0], bola[1] + tamanho)
            elif bola[1] == (600 - tamanho):
                direcao_y_bola = CIMA
    
    if direcao_y_bola == CIMA:
        if bola[1] > tamanho:
            bola = (bola[0], bola[1] - tamanho)
        elif bola[1] == tamanho:
            direcao_y_bola = BAIXO

    if direcao_x_bola == ESQUERDA:
        if bola[0] >= tamanho:
            bola = (bola[0] - tamanho, bola[1])
        elif bola[0] == 0:
            direcao_x_bola = DIREITA
    if direcao_x_bola == DIREITA:
        if bola[0] < (600 - tamanho):
            bola = (bola[0] + tamanho, bola[1])
        elif bola[0] == (600 - tamanho):
            direcao_x_bola = ESQUERDA
                    
    # Move a raquete para a esquerda
    if direcao == ESQUERDA:
        for bloco in range(len(raquete)):
            posicao_minima = tamanho * bloco
            if raquete[bloco][0] > posicao_minima:
                raquete[bloco] = (raquete[bloco][0] - tamanho, (600 - tamanho))
    
    # Move a raquete para a direita
    if direcao == DIREITA:
            for bloco in range(len(raquete)):
                posicao_maxima = 600 - (len(raquete) - bloco) * tamanho
                if raquete[bloco][0] < posicao_maxima:
                    raquete[bloco] = (raquete[bloco][0] + tamanho, (600 - tamanho))

    # Faz a contagem dos pontos   
    if bola[1] == 600 - tamanho:
        if bola[0] >= min(raquete)[0] and bola[0] <= max(raquete)[0]:
            pontos += 1
        else:
            # Faz o fim do jogo
            if tentativas < max_tentativas:
                bola = posicao_bola()
                tentativas += 1
                pontos = 0
            else:
                bola = (bola[0], 600)
                texto = fonte.render('Fim de Jogo', 1, (255, 255, 255))
                tela.blit(texto, (170,270))
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
    pygame.display.update()
    
