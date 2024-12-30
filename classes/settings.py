import pygame

class Settings:

    def __init__(self, game):
        self.game = game

        self.screen_width = 900
        self.screen_height = 600

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snowball Battle')

        #fonts
        self.gamefont = pygame.font.Font('font/funky.ttf', 50)
        self.smallgamefont = pygame.font.Font('font/funky.ttf', 30)
        self.statsfont = pygame.font.SysFont('impact', 30, bold=False)
        
        #backgorund
        self.background_image = pygame.image.load('images/background.png')
        self.background_rect = self.background_image.get_rect()
        self.background_y = -self.background_rect.height

        #music
        self.music = pygame.mixer.music.load('music/xmas-music.mp3')
        pygame.mixer.music.set_volume(0.05)
        
    