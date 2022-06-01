import pygame  # main lib for this project
import os   #lib to manipulate path on os
import random  # gerenate random

TELA_LARGURA = 500  # constants screen size
TELA_ALTURA = 800  # constants screen size

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))  # pygame only see locale
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGENS_PASSARO = [ # this is a list in python
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]

pygame.font.init()  # initialize font type of text that will be used
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

# CREATE OBJECTS OF THE GAME (THINGS THAT MOVE OR NOT. BIRD, PIPES E FLOOR)


class Passaro:
    IMGS = IMAGENS_PASSARO
    # ROTATION'S ANIMATIONS
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5  # time to change the bird

    def __init__(self, x, y):  # bird's attributes | def __init__ it's the initial  functionalities
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0;  # parabolic move time
        self.contagem_imagem = 0  # identify current image used
        self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y  # last height before last jump

    def mover(self):
        # calulate displacement
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo ** 2) + self.velocidade * self.tempo

        # contrain displacement
        if deslocamento > 16:  # max vertical displacement
            deslocamento = 16
        elif deslocamento < 0:  # increment for the jump height
            deslocamento -= 2

        self.y += deslocamento
        # bird's angle
        if deslocamento < 0 or self.y (self.altura + 50):  # if the bird's still above initical height before jump
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:  # max = -90º
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # define witch bird image will be used
        self.contagem_imagem += 1  # when pass TEMPO_ANIMACAO change image

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:  # if contagem_imagem is less then 10
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:  # if contagem_imagem is less then 15
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:  # reverse clapping
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # if the bird is falling don't clap wings
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2  # if is falling the next clap will be down(IMGS[2])

        # draw the image | this is how rotate image around the center with pygame
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)  # rotate image
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)  # it's like pygame draw an retangle around the image and paste in the screen
        tela.blit(imagem_rotacionada, retangulo.topleft)  # drawing in the screen with pygame

    def get_mask(self):  # gets mask from bird's image
        pygame.mask.from_surface(self.imagem)




