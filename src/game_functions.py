import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, fi_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(fi_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullets(fi_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    if len(bullets) < fi_settings.bullets_allowed:
        new_bullet = Bullet(fi_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(fi_settings, screen, stats, play_button, ship, aliens, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(fi_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, fi_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(fi_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks PLAY"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # reset game stats
        stats.reset_stats()
        stats.game_active = True

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet and center the ship
        create_fleet(fi_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(fi_settings, screen, stats, ship, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(fi_settings.bg_color)

    # Redraw all bullets behind ship and aliens
    for (
        bullet
    ) in bullets.sprites():  # why iterate over bullets.sprites() if just bullets work??
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # draw play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(fi_settings, screen, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets"""
    # update position
    bullets.update()

    # get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(fi_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collision(fi_settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collisions"""
    # check for any bullets that have hit aliens
    # if so, get rid of the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # destroy existing bullets and create new fleet
        bullets.empty()
        create_fleet(fi_settings, screen, ship, aliens)


def get_number_aliens_x(fi_settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = fi_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(fi_settings, ship_height, alien_height):
    """Determine the number of rows of aliens"""
    available_space_y = (
        fi_settings.screen_height - 3 * alien_height - ship_height
    )  # 2 extra alien_heights to give player enough time to start shooting
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(fi_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row"""
    alien = Alien(fi_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(fi_settings, screen, ship, aliens):
    """Create full fleet of aliens"""
    # create an alien and find the number of aliens in a row
    # spacing between aliens is equal to one alien width
    alien = Alien(fi_settings, screen)
    number_aliens_x = get_number_aliens_x(fi_settings, alien.rect.width)
    number_rows = get_number_rows(fi_settings, ship.rect.height, alien.rect.height)

    # create fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(fi_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(fi_settings, aliens):
    """Respond if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(fi_settings, aliens)
            break


def change_fleet_direction(fi_settings, aliens):
    """Drop entire fleet and change its direction"""
    for alien in aliens.sprites():
        alien.rect.y += fi_settings.fleet_drop_speed
    fi_settings.fleet_direction *= -1


def ship_hit(fi_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien"""
    if stats.ships_left > 0:
        # decrement ships_left
        stats.ships_left -= 1

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet and center the ship
        create_fleet(fi_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(1.2)

    else:
        stats.game_active = False


def check_aliens_bottom(fi_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # treat this the same as if the ship got hit
            ship_hit(fi_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(fi_settings, stats, screen, ship, aliens, bullets):
    """Check if the fleet is at an edge and update the positions of all aliens in the fleet"""
    check_fleet_edges(fi_settings, aliens)
    aliens.update()

    # look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(fi_settings, stats, screen, ship, aliens, bullets)

    # look for aliens hitting the bottom of the screen
    check_aliens_bottom(fi_settings, stats, screen, ship, aliens, bullets)
