import os
import pygame as pg

pg.init()

# Tela
largura = 400
altura = 300
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption("Meu Jogo")

# Carregar imagem
caminho_personagem = os.path.join(os.path.dirname(__file__), "personagem.png")
personagem = pg.image.load(caminho_personagem)
personagem = pg.transform.scale(personagem, (110, 110))  # redimensiona

# Posição
x = 200
y = 150
velocidade = 5

# Cores
azul = (0, 0, 255)

clock = pg.time.Clock()
rodando = True

while rodando:
    clock.tick(60)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False

    teclas = pg.key.get_pressed()

    if teclas[pg.K_LEFT]:
        x -= velocidade
    if teclas[pg.K_RIGHT]:
        x += velocidade
    if teclas[pg.K_UP]:
        y -= velocidade
    if teclas[pg.K_DOWN]:
        y += velocidade

    # Fundo
    tela.fill(azul)

    # Desenhar personagem (imagem)
    tela.blit(personagem, (x, y))

    pg.display.flip()

pg.quit()

