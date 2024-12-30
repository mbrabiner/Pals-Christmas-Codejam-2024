import pygame
import sys
from pygame.locals import *
import time


class WelcomeScreen():
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.settings.screen
        self.welcome = 'Snowball Battle'
        self.welcomeSurface = self.settings.gamefont.render(self.welcome, True, (4, 48, 79))
        self.welcomeRect = self.welcomeSurface.get_rect()
        self.welcomeRect.midtop = (self.settings.screen_width / 2, self.settings.screen_height / 4)


        self.play = 'Press Enter to Play'
        self.playSurface = self.settings.smallgamefont.render(self.play, True, (4, 48, 79))
        self.playRect = self.playSurface.get_rect()
        self.playRect.midtop = (self.settings.screen_width / 2, self.settings.screen_height / 2)

    def show_screen(self):
        while not self.game.running:
            self.settings.screen.blit(self.settings.background_image, self.settings.background_rect)
            self.screen.blit(self.welcomeSurface, self.welcomeRect)
            self.screen.blit(self.playSurface, self.playRect)  # Render the welcome text

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.game.running = True  # Start the game
                



class GameOver():
    def __init__(self, game, winner):
        self.game = game
        self.settings = game.settings
        self.screen = game.settings.screen

        self.game_over_text = 'Game Over!'
        self.game_over_textSurface = self.settings.gamefont.render(f'{self.game_over_text}', True, (4, 48, 79))
        self.game_over_textRect = self.game_over_textSurface.get_rect()
        self.game_over_textRect.midtop = (self.settings.screen_width/2, self.settings.screen_height/4)

        self.winner = game.winner
        self.winnerSurface = self.settings.gamefont.render(f'{winner}', True, (4, 48, 79))
        self.winnerRect = self.winnerSurface.get_rect()
        self.winnerRect.midtop = (self.settings.screen_width/2, self.settings.screen_height/1.9)

        self.play_again = 'Press Enter to Play Again'
        self.play_againSurface = self.settings.smallgamefont.render(f'{self.play_again}', True, (4, 48, 79))
        self.play_againRect = self.play_againSurface.get_rect()
        self.play_againRect.midtop = (self.settings.screen_width/2, self.settings.screen_height/1.5)

    def show_screen(self):
        start_time = time.time()
        
        while not self.game.running:
            elapsed_time = time.time() - start_time
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN and elapsed_time > 4:  # If Enter is pressed, game starts
                        # Reinitialize the game state
                        self.game.__init__(True)
                        self.game.run()
                        return
                    
                self.settings.screen.blit(self.game_over_textSurface, self.game_over_textRect)
                self.settings.screen.blit(self.winnerSurface, self.winnerRect)
                self.settings.screen.blit(self.play_againSurface, self.play_againRect)

            pygame.display.flip()
        

        