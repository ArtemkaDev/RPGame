import pygame


class Solider(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed,screen):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load('img/players/default/Layer 1.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen
    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        self.rect.x += dx
        self.rect.y += dy
