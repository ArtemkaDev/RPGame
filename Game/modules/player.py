import pygame
import time

#global values
gravity = 0.75
prev_time = time.time()

class Solider(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, screen):
        pygame.sprite.Sprite.__init__(self)
        self.prev_time = prev_time
        self.dt = 0
        self.alive = True
        self.scale = scale
        self.speed = speed
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.flip = False
        self.char_type = char_type
        self.update_time = pygame.time.get_ticks()
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f'img/players/{self.char_type}/stay/{i}.png').convert()
            img = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f'img/players/{self.char_type}/run/{i}.png').convert()
            img = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen

    def draw(self):
        self.dt = time.time() - self.prev_time
        self.dt *= 60
        self.prev_time = time.time()
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_left:
            self.flip = True
            dx = -self.speed * self.dt
        if moving_right:
            self.flip = False
            dx = self.speed * self.dt
        if self.jump == True:
            self.vel_y = 0
            self.jump = False
        '''self.vel_y += gravity
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y'''

        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        #update anim
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        #check if actions have difference
        if new_action != self.action:
            self.action = new_action
            #upd anim sett
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

