import pygame
import sys
from classes.characters import User1, User2
from classes.settings import Settings
from classes.snowballs import Snowball
from classes.snowbullets import Snowbullet
from classes.screens import GameOver, WelcomeScreen


class Game:
    def __init__(self, running=False):
        pygame.init()
        
        self.settings = Settings(self)
        self.screen = self.settings.screen
        self.user1 = User1(self)
        self.user2 = User2(self)

        self.snowball = Snowball(self)

        self.snowbullets = pygame.sprite.Group()
        self.snowballs = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.running = running

        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.current_seconds = 45

        pygame.mixer.music.play(-1)

        pygame.key.set_repeat(0) 


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # check if exit clicked
                pygame.mixer.music.stop()
                sys.exit()
            if event.type == pygame.USEREVENT:
                self.current_seconds -= 1
                if self.current_seconds <= -1:
                    self.running = False
                    if self.user1.score > self.user2.score:
                        self.winner = 'Player 1 Wins!'
                    elif  self.user1.score < self.user2.score:
                        self.winner = 'Player 2 Wins!'
                    else:
                        self.winner = 'Its a draw!!!'
                    print(f"Winner determined: {self.winner}")
                    GameOver(self, self.winner).show_screen()

            elif event.type == pygame.USEREVENT + 1: #adding snowballs
                self.add_snowball()
            elif event.type == pygame.KEYDOWN:
                    self.check_key_events_player1(event, True) #check if moving 
                    self.check_key_events_player2(event, True)  
            elif event.type == pygame.KEYUP:
                    self.check_key_events_player1(event, False) #check if stopped moving
                    self.check_key_events_player2(event, False) 

    def add_snowball(self):
        new_snowball = Snowball(self) #create new snowball instance
        self.snowballs.add(new_snowball) #add instance to snowballs sprite group
        self.all_sprites.add(new_snowball) # add instance to all sprites???
        

    def pick_up(self):
        for snowball in self.snowballs: 
            if pygame.sprite.collide_rect(self.user1, snowball):
                self.user1.throws += 1 # get a snowball
                snowball.kill() #snowball removed from screen
            elif pygame.sprite.collide_rect(self.user2, snowball):
                self.user2.throws += 1
                snowball.kill()


    def throw_snowbullet(self, firing_user):
        """Fire a snowbullet from the specified user."""
        if firing_user == 'user1' and self.user1.throws > 0:
            new_snowbullet = Snowbullet(self, 'user1')  # Pass 'user1' as firing_user
            self.snowbullets.add(new_snowbullet)
            self.user1.throws -= 1  # Reduce available throws for user1
            #print("User1 fired a bullet")  
        elif firing_user == 'user2' and self.user2.throws > 0:
            new_snowbullet = Snowbullet(self, 'user2')  # Pass 'user2' as firing_user
            self.snowbullets.add(new_snowbullet)
            self.user2.throws -= 1  # Reduce available throws for user2
            #print("User2 fired a bullet") 


    def update_snowbullets(self):
        self.snowbullets.update()
        # Remove bullets that go out of bounds
        for snowbullet in self.snowbullets.copy():
            if snowbullet.rect.left <= 0 or snowbullet.rect.right >= 800:
                self.snowbullets.remove(snowbullet)
        
    def hit(self):
        for snowbullet in self.snowbullets.copy():
            if pygame.sprite.collide_rect(self.user1, snowbullet): 
                if snowbullet.firing_user == 'user2':  # Only count hits from user2's bullets
                    self.user2.score += 5
                    snowbullet.kill()  # Remove the bullet after collision
            elif pygame.sprite.collide_rect(self.user2, snowbullet):
                if snowbullet.firing_user == 'user1':  # Only count hits from user1's bullets
                    self.user1.score += 5
                    snowbullet.kill()  # Remove the bullet after collision

    def check_key_events_player1(self, event, movement_status: bool): 
        if event.key == pygame.K_a:
            self.user1.moving_left = movement_status
        elif event.key == pygame.K_d:
            self.user1.moving_right = movement_status
        elif event.key == pygame.K_w:
            self.user1.moving_up = movement_status
        elif event.key == pygame.K_s:
            self.user1.moving_down = movement_status
        elif event.key == pygame.K_SPACE and movement_status:  # Fire when SPACE is pressed
            self.throw_snowbullet('user1')

    def check_key_events_player2(self, event, movement_status: bool):
        if event.key == pygame.K_LEFT:
            self.user2.moving_left = movement_status
        elif event.key == pygame.K_RIGHT:
            self.user2.moving_right = movement_status
        elif event.key == pygame.K_UP:
            self.user2.moving_up = movement_status
        elif event.key == pygame.K_DOWN:
            self.user2.moving_down = movement_status
        elif event.key == pygame.K_RETURN and movement_status:  # Fire when RETURN is pressed
            self.throw_snowbullet('user2')

    
    def draw_sprites_on_screen(self):
        time_text = self.settings.statsfont.render(f'{self.current_seconds}', False, (4, 48, 79)) #display scores and snowballs
        self.screen.blit(time_text, (400, 15))
        user1_snowballs = self.settings.statsfont.render(f'Snowballs: {self.user1.throws}', False, (4, 48, 79)) #display scores and snowballs
        self.settings.screen.blit(user1_snowballs, (20, 15))
        user1_score = self.settings.statsfont.render(f'Score: {self.user1.score}', False, (4, 48, 79))
        self.settings.screen.blit(user1_score, (20, 40))


        user2_snowballs = self.settings.statsfont.render(f'Snowballs: {self.user2.throws}', False, (4, 48, 79))
        self.settings.screen.blit(user2_snowballs, (630, 15))
        user2_score = self.settings.statsfont.render(f'Score: {self.user2.score}', False, (4, 48, 79))
        self.settings.screen.blit(user2_score, (630, 40))

        self.screen.blit(self.user1.image, self.user1.rect) # blit characters
        self.screen.blit(self.user2.image, self.user2.rect)

        for entity in self.all_sprites:
            self.settings.screen.blit(entity.image, entity.rect)

        for snowbullet in self.snowbullets:  # Explicitly draw bullets if needed
            snowbullet.draw_bullet()
           # print("Drawing bullet") 

    def run(self):
        if not self.running:
            welcome_screen = WelcomeScreen(self)
            welcome_screen.show_screen()

        while self.running:
            self.check_events()
            self.user1.update()
            self.user2.update()
            self.snowball.update()
            self.pick_up()
            self.hit()
            self.update_snowbullets()
            self.settings.screen.blit(self.settings.background_image, self.settings.background_rect)
            
            self.draw_sprites_on_screen()

            pygame.display.flip()
            self.clock.tick(30)
                 
                 




if __name__ == '__main__':
    game = Game(False)
    game.run()