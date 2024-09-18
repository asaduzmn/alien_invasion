import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    #Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #Make a ship
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()    

    #Start the main loop for the game
    while True:
        #watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()   

        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        #create fleet of aliens
        gf.create_fleet(ai_settings, screen, ship, aliens)


        #update the screen
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
run_game()
