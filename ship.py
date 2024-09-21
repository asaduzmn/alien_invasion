import pygame

class Ship:
    def __init__(self, ai_game) -> None:
        """
        initialize the ship and set its starting position
        """
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom


        # #store decimal value of the ship's center for moving_factor fraction value
        # self.center = float(self.rect.centerx)

        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # moving flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """
        Update the ship's position based on the movement flag.
        """       
        #update the ship's x value, not the rect.
        if self.moving_right  and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left>0:
            self.x -= self.settings.ship_speed
        
        #update the rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current locationq
        """
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """
        Center the ship on the screen
        """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    