import pygame
from pygame.sprite import Sprite

class  Characters(Sprite):
    def __init__(self, game):
        self.screen = game.settings.screen
        self.screen_rect = game.settings.screen.get_rect()
        self.score = 0
        self.throws = 5

        # default movement status
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

class User1(Characters):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load('images/peng1.png')
        self.rect = self.image.get_rect()   
        self.rect.midleft = self.screen_rect.midleft

        
    def update(self):
        if self.moving_right:
            self.rect.move_ip(5, 0)
        if self.moving_left:
            self.rect.move_ip(-5, 0)
        if self.moving_up:
            self.rect.move_ip(0, -5)
        if self.moving_down:
            self.rect.move_ip(0, 5)


        # Keep player on the left half of screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 450:
            self.rect.right = 450   
        if self.rect.top <= 0:
            self.rect.top = 0   
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            

class User2(Characters):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load('images/peng2.png')
        self.rect = self.image.get_rect()   
        self.rect.midright = self.screen_rect.midright

    def update(self):
        if self.moving_right:
            self.rect.move_ip(5, 0)   
        if self.moving_left:
            self.rect.move_ip(-5, 0)           
        if self.moving_up:
            self.rect.move_ip(0, -5)
        if self.moving_down:
            self.rect.move_ip(0, 5)

        # Keep player on right half of screen
        if self.rect.left < 450:
            self.rect.left = 450
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

