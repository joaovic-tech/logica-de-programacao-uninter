import pygame
from pygame import Surface, Rect

W_WIDTH = 576
W_HEIGHT = 324

# Inicializar o Módulo do PyGame
pygame.init()
print('setup start')

# Criação de janela do pygame
screen: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

# Carregar imagem e gerar uma superfície
background_surf: Surface = pygame.image.load('asset/background.png').convert_alpha()
player1_surf: Surface = pygame.image.load('./asset/player1.png').convert_alpha()

# Obter o retângulo da superfície
background_rect: Rect = background_surf.get_rect(left=0, top=0)
player1_rect: Rect = player1_surf.get_rect(left=100, top=100)

# Desenhar na janela (window)
screen.blit(source=background_surf, dest=background_rect)
screen.blit(source=player1_surf, dest=player1_rect)

# Atualizar a janela
pygame.display.flip()

# Colocar um relógio no nosso jogo
clock = pygame.time.Clock()

# Carregar musica e deixar ela tocando
pygame.mixer_music.load('./asset/fase1.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.3)
print('setup end')
print('loop start')

while True:
    clock.tick(60)  # esse loop está acontecendo 230 vezes por segundo
    
    print(f'{clock.get_fps() :.0f}')  # executar o print o fps
    
    screen.blit(source=background_surf, dest=background_rect)
    screen.blit(source=player1_surf, dest=player1_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop end')
            pygame.quit()
            quit()

    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
        pass
