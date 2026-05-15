import pygame

pygame.init()

# Tela
largura = 400
altura = 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo")

# Carregar imagem
personagem = pygame.image.load("personagem.png")
personagem = pygame.transform.scale(personagem, (110, 110))  # redimensiona

# Posição
x = 200
y = 150
velocidade = 5

# Cores
preto = (0, 0, 0)

clock = pygame.time.Clock()
rodando = True

while rodando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Fundo
    tela.fill(preto)

    # Desenhar personagem (imagem)
    tela.blit(personagem, (x, y))

    pygame.display.flip()

pygame.quit()

