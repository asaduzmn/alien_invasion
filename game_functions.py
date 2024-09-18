import sys
import pygame


def check_keydown_events(event, ship):
    """Respond to keypresses

    Args:
        event (pygame key): check keyboard event
        ship (Ship): holds characteristics of ship
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_up_events(event, ship):
    """Respond to key releases

    Args:
        event (pygame key): check keyboard event
        ship (Ship): holds characteristics of ship
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



def check_events(ship):
    """Respond to keypresses and mouse event
    """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ship)
            elif event.type == pygame.KEYUP:
                check_up_events(event, ship)
                


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