import pygame
import sys
from pygame.sprite import Group
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """
    Overall class to manage game assets and behavior
    """
    def __init__(self) -> None:
        """Initializw the game and create fame resources
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #create an instance to store game statistics,
        # and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = Group()
        self.aliens = Group()

        self._create_fleet()

        #start game in inactive stat
        self.game_active = False

        #make play button
        self.play_button = Button(self, 'Play')
    

    def run_game(self):       
        #Start the main loop for the game
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)


    def _ship_hit(self):
        """
        Respond to the ship being hit by an alien.
        """
        if self.stats.ships_left > 0:
            #decrement ships_left
            self.stats.ships_left -= 1

            #get rid of any remaining alien and bullet
            self.bullets.empty()
            self.aliens.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """
        Check if any aliens have reached the bottom of the screen
        """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat this the same as if the ship got hit
                self._ship_hit()
                break


    def _update_aliens(self):
        """
        Check if the fleet is at an edge, and
        then update the positons of all aliens in the fleet
        """
        self._check_fleet_edges()
        self.aliens.update()

        #look got alien.ship collisons
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    
    def _check_fleet_edges(self):
        """
        Respond appropriately if any aliens have reached and edge.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """
        Drop the entire fleet and chage the fleets direction
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        
        self.settings.fleet_direction *=-1


    def _check_events(self):
        """Respond to keypresses and mouse events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_up_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_po):
        """
        Strt a new game when the player clicks play
        """
        button_clicked = self.play_button.rect.collidepoint(mouse_po)
        if button_clicked and not self.game_active:
            #reset the game settings
            self.settings.initialize_dynamic_settings()
            #reset the game statistics
            self.stats.reset_stats()
            self.sb.prep_score()
            self.game_active = True

            #get rid of any remaining alien and bullet
            self.bullets.empty()
            self.aliens.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #hide mouse cursor
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """Respond to keypresses

        Args:
            event (pygame key): check keyboard event
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    
    def _check_up_events(self, event):
        """Respond to key releases

        Args:
            event (pygame key): check keyboard event
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """
        Fire a bullet if limit not reached yet
        """
        #create a new bullet and add it to the bullets group.
        if  len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    
    def _update_bullets(self):
        """
        Update position of bullets and get rid of old bullets
        """
        #update bullet position
        self.bullets.update()

        #get rid of bullets that disappeard
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collision()


    def _check_bullet_alien_collision(self):
        """
        Respond to bullet-alien collision
        """
        #remove bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()

        if not self.aliens:
            #destroy existing bullters and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increse_speed()


    def _update_screen(self):
        """
        Update images on the screen and flip to the new screen
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #draw score information
        self.sb.show_score()

        #draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        

    def _create_fleet(self):
        """
        Create a full fleet of aliens
        """
        #create an alien and find the number of aliens in a row.
        #spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # available_space = self.settings.screen_width - 2*alien_width
        # number_alien_x = available_space // (2*alien_width)

        # """
        # Determine the number of rows of aliens that fit on the screen.
        # """
        # ship_height = self.ship.rect.height
        # available_space_y = (self.settings.screen_height - 
        #                     (3 * alien_height) - ship_height)
        # number_rows = available_space_y//(2*alien_height)

        # # number_alien_x = get_number_alien_x(ai_settings, alien_width)
        # # number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

        # # #create fleet of aliens
        # for row_number in range(number_rows):
        #     for alien_number in range(number_alien_x):
        #         self._create_alien(alien_number, row_number)
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3*alien_height - self.ship.rect.height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width
            
            #finished a row; reset x value, and increment y value
            current_x = alien_width
            current_y += 2*alien_height


    def _create_alien(self, x_postion, y_postion):
        """
        Create an alien and place it in the row
        """
        new_alien = Alien(self)
        # alien_width = alien.rect.width
        new_alien.x = x_postion
        new_alien.rect.x = x_postion
        new_alien.rect.y = y_postion
        self.aliens.add(new_alien)



if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
