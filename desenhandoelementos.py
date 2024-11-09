import pygame
# Inicializar o pygame
pygame.init()

tamanho = (900, 500)
# Cria uma tela com tamanho especificado
tela = pygame.display.set_mode(tamanho)

# Define o título da janela
pygame.display.set_caption("Hello Games!")

# Define um relógio para controlar o FPS
relogio = pygame.time.Clock()

posicaoBola = pygame.Vector2(450, 250)
dt = 0
direcaoY = direcaoX = 1
velBola = 200

while True:
    # Lida com os eventos da aplicação
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit() # Fechando o pygame

    # Preenche a tela com uma cor
    tela.fill((40, 200, 100))

    # Desenha um circulo na tela
    bola = pygame.draw.circle(tela, (10, 255, 200), posicaoBola, 50)

    posicaoBola.y += velBola * direcaoY * dt
    posicaoBola.x += velBola * direcaoX * dt

    if posicaoBola.y >= 450 or posicaoBola.y <= 50:
        direcaoY *= -1 # Inverte a direção

    if posicaoBola.x >= 850 or posicaoBola.x <= 50:
        direcaoX *= -1 # Inverte a direção

    # Atualiza a tela
    pygame.display.update()
    dt = relogio.tick(60) / 1000 # Define a quantidade de FPS