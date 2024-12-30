import pygame
from pygame.sprite import Sprite
import random


class Snowball(Sprite):
    '''class to manage snowballs picked up'''

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.settings.screen
        self.settings = game.settings
        self.screen_rect = game.settings.screen.get_rect()

        self.add_snow_ball_timer()

        # Loading the snowball image and rect
        self.image = pygame.image.load('images/snoball3.png')
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, 800 - self.rect.width)  # Random x within screen width
        self.rect.y = random.randint(100, 600 - self.rect.height)  # Random y within screen width, not in stats area


    def add_snow_ball_timer(self, interval=700):
        add_snowball = pygame.USEREVENT + 1
        pygame.time.set_timer(add_snowball, interval)




