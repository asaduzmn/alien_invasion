import sys
import pygame

def check_events():
    """Respond to keypresses and mouse event
    """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen

    Args:
        ai_settings (Settings): object of Settings class
        screen (pygame): screen of the game
        ship (Ship): store all characteristics of Ship
    """
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()