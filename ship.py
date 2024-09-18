import pygame

class Ship():
    def __init__(self, ai_settings, screen) -> None:
        """
        initialize the ship and set its starting position
        """
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

        #store decimal value of the ship's center for moving_factor fraction value
        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """
        Update the ship's position based on the movement flag.
        """

        #update the ship's center value, not the rect.
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        
        #update the rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current locationq
        """
        self.screen.blit(self.image, self.rect)
    