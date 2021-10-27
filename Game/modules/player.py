import pygame


class Solider(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed,screen):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.speed = speed
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(5):
            img = pygame.image.load(f'img/players/default/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed
        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        #update anim
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0