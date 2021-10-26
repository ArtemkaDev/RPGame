import pygame

class Solider(pygame.sprite.Sprite):
    def __init__(self, x, y ,scale):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('img/Layer 1.png')
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)