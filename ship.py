import pygame

class Ship():
    #prepare ship.bmp to load into screen
    def __init__(self, screen, ai_settings):
        #initialize the screen position
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get it's rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship athe bottom ceter of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #moving flag
        self.moving_right = False
        self.moving_left = False

        #storing ship position 
        self.center = float(self.rect.centerx)

    def update(self):
        #update the position of ship based on movement flag
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center

    def blitme(self):
        #Draw the current location of the ship
        self.screen.blit(self.image, self.rect)
