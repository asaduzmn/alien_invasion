import pygame

class Ship():
    def __init__(self, screen) -> None:
        """
        tialize the ship and set its starting position
        """
        self.screen = screen

        #load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        """Draw the ship at its current locationq
        """
        self.screen.blit(self.image, self.rect)
    