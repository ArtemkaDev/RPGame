import pygame


class Solider(pygame.sprite.Sprite):
    def __init__(self, x, y ,scale, screen):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        img = pygame.image.load('img/Layer 1.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen
    def draw(self):
        self.screen.blit(self.image, self.rect)