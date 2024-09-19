import sys
import pygame

from bullet import Bullet
from alien import Alien


def fire_bullet(ai_settings, screen, ship, bullets):
    """
    Fire a bullet if limit not reached yet
    """
    #create a new bullet and add it to the bullets group.
    if  len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses

    Args:
        event (pygame key): check keyboard event
        ai_settings(Setings) : settings of this game
        screen(pygame) : display
        bullets(Group): groups of bullets 
        ship (Ship): holds characteristics of ship
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


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
    elif event.key == pygame.K_q:
        sys.exit()



def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse event
    """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_up_events(event, ship)
                


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen

    Args:
        ai_settings (Settings): object of Settings class
        screen (pygame): screen of the game
        ship (Ship): store all characteristics of Ship\
        bullets(Group): group of bullets
    """
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    


def update_bullets(bullets):
    """
    Update position of bullets and get rid of old bullets.
    """
    #update bullet positions
    bullets.update()

    #get rid of bullets that disappeard
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_alien_x(ai_settings, alien_width):
    """
    Determine the number of aliens that fit in a row
    """
    available_space = ai_settings.screen_width - 2*alien_width
    number_alien_x = int(available_space / (2*alien_width))

    return number_alien_x


def create_alien(ai_settings, screen, aliens, alien_number):
    """
    Create an alien and place it in the row
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
    


def create_fleet(ai_settings, screen, aliens):
    """
    Create a full fleet of aliens
    """
    #create an alien and find the number of aliens in a row.
    #spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_alien_x = get_number_alien_x(ai_settings, alien_width)

    #create the first row of aliens
    for alien_number in range(number_alien_x):
        #create an alien and place it in the row
        create_alien(ai_settings, screen, alien_number)