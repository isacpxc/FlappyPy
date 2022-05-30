import pygame; # main lib for this project
import os;  #lib to manipulate path on os
import random; # gerenate random

TELA_LARGURA = 500; # constants screen size
TELA_ALTURA = 800; # constants screen size

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png'))); # pygame only see locale
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')));
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')));
IMAGENS_PASSARO = [ # this is a list in python
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
];

pygame.font.init(); # initialize font type of text that will be used
FONTE_PONTOS = pygame.font.SysFont('arial', 50);
