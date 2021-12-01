import pygame
import time

# global values
gravity = 0.75


class Solider(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale_x, scale_y, speed, screen, proc_x, proc_y):
        pygame.sprite.Sprite.__init__(self)
        self.proc_x = proc_x
        self.proc_y = proc_y
        self.prev_time = time.time()
        self.dt = 0
        self.alive = True
        self.scale_x = scale_x * self.proc_x
        self.scale_y = scale_y * self.proc_y
        self.speed = speed
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.flip = False
        self.moving_left = False
        self.moving_right = False
        self.char_type = char_type
        self.update_time = pygame.time.get_ticks()
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f'img/players/{self.char_type}/stay/{i}.png').convert()
            img = pygame.transform.scale(img, (int(self.scale_x), int(self.scale_y)))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f'img/players/{self.char_type}/run/{i}.png').convert()
            img = pygame.transform.scale(img, (int(self.scale_x), int(self.scale_y)))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x*self.proc_x, y*self.proc_y)
        self.screen = screen

    def draw(self):
        self.dt = time.time() - self.prev_time
        self.dt *= 60
        self.prev_time = time.time()
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def move(self):
        dx = 0
        dy = 0
        if self.moving_left:
            self.flip = True
            dx = -self.speed * self.dt
        if self.moving_right:
            self.flip = False
            dx = self.speed * self.dt
        if self.jump == True:
            self.vel_y = 10 * self.dt * -1
            self.jump = False
        #gravity
        self.vel_y += gravity
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y * self.dt

        if self.rect.bottom + dy > 180 * self.proc_y:
            dy = 180 * self.proc_y - self.rect.bottom

        #update
        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        # update anim
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        # check if actions have difference
        if new_action != self.action:
            self.action = new_action
            # upd anim sett
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
