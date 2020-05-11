import pygame, random
from pygame.locals import *

bloco = 10
max_tentativas = 5

def posicao_maca():
    """ Gera uma posição aleatória para a maçã"""
    return (random.randint(0, 59) * 10, random.randint(0, 59) * 10)

# Cria as direções para onde a cobra pode andar
CIMA = 'CIMA'
BAIXO = 'BAIXO'
DIREITA = 'DIREITA'
ESQUERDA = 'ESQUERDA'

# Inicia a tela
pygame.init()
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

# Cria a cobra
cobra_inicio = [(200, 200), (200, 200 + bloco), (200, 200 + 2 * bloco)]
cobra = cobra_inicio[:]
textura_cobra = pygame.Surface((bloco, bloco))
textura_cobra.fill((255, 255, 255))
direcao_cobra = DIREITA

# Cria a Maçã
maca = posicao_maca()
textura_maca = pygame.Surface((bloco, bloco))
textura_maca.fill((255, 0, 0))

# Cria a contagem de pontos e de tentativas
pontos = 0
tentativas = 1

temporizador = pygame.time.Clock()

# Inicia a fonte
pygame.font.init()
fonte_padrao = pygame.font.get_default_font()
fonte = pygame.font.SysFont(fonte_padrao, 60)

for i in range(3, -1, -1):
    texto = fonte.render(f'O jogo vai começar em {i}...', 1, (255, 255, 255))
    tela.blit(texto, (40, 270))
    pygame.display.update()
    pygame.time.delay(1000)
    tela.fill((0, 0, 0))

contador = 0

while True:
    temporizador.tick(30)
        
    for event in pygame.event.get():    
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                direcao_cobra = CIMA
                
            if event.key == K_DOWN:
                direcao_cobra = BAIXO
            
            if event.key == K_RIGHT:
                direcao_cobra = DIREITA
            
            if event.key == K_LEFT:
                direcao_cobra = ESQUERDA
                
    # Movimento
    for pos in range(len(cobra) - 1, 0, -1):
        cobra[pos] = (cobra[pos - 1][0], cobra[pos - 1][1])
    
    if direcao_cobra == CIMA:
        cobra[0] = (cobra[0][0], cobra[0][1] - bloco)
    if direcao_cobra == BAIXO:
        cobra[0] = (cobra[0][0], cobra[0][1] + bloco)
    if direcao_cobra == DIREITA:
        cobra[0] = (cobra[0][0] + bloco, cobra[0][1])
    if direcao_cobra == ESQUERDA:
        cobra[0] = (cobra[0][0] - bloco, cobra[0][1])
                
    # Ponto
    if cobra[0] == maca:
        cobra.append(cobra[len(cobra) - 1])
        maca = posicao_maca()
        pontos += 1
    
    # Morte
    if cobra[0][0] < 0 or cobra[0][0] > (600 - bloco) or cobra[0][1] < 0 or cobra[0][1] > (600 - bloco):
        cobra = cobra_inicio[:]
        direcao_cobra = DIREITA
        maca = posicao_maca()
        pontos = 0
        tentativas += 1
        pygame.time.delay(1000)
    
    # Fim do Jogo
    if tentativas == max_tentativas + 1:
        texto = fonte.render(f'Fim de Jogo!', 1, (255, 255, 255))
        tela.blit(texto, (170, 270))    
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()

    tela.fill((0, 0, 0))
    
    # Atualização movimento da cobra
    for pos in cobra:
        tela.blit(textura_cobra, pos)
    
    tela.blit(textura_maca, maca)
    
    texto = fonte.render(f'Pontos: {pontos}, Tentativas: {tentativas}', 1, (255, 255, 255))
    tela.blit(texto, (0, 0))
    
    pygame.display.update()
    
    
