import pygame 
class Snowbullet(pygame.sprite.Sprite):  # Ensure it inherits from Sprite
    def __init__(self, game, firing_user):
        super().__init__()
        self.game = game
        self.firing_user = firing_user  # Set the firing user ('user1' or 'user2')
        
        # Load the snowbullet image
        self.image = pygame.image.load('images/snoball3.png')
        self.rect = self.image.get_rect()

        # Set the starting position of the bullet based on the firing user
        if self.firing_user == 'user1':
            self.rect.midright = game.user1.rect.midright  # Start at user1's position
            self.speed = 13  # Move to the right
 
        elif self.firing_user == 'user2':
            self.rect.midleft = game.user2.rect.midleft  # Start at user2's position
            self.speed = -13  # Move to the left


        self.x = float(self.rect.x)  # Store x position as float for precise movement

    def update(self):
        self.x += self.speed  # Update position based on speed
        self.rect.x = int(self.x)  # Update rect position


    def draw_bullet(self):
        self.game.screen.blit(self.image, self.rect)

