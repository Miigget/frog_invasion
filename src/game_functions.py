import sys
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

def check_events(fi_settings, screen, ship, bullets):
  """Respond to keypresses and mouse events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, fi_settings, screen, ship, bullets)

    elif event.type == pygame.KEYUP:
      check_keyup_events(event, ship)

def update_screen(fi_settings, screen, ship, aliens, bullets):
  """Update images on the screen and flip to the new screen"""
  # Redraw the screen during each pass through the loop
  screen.fill(fi_settings.bg_color)

  # Redraw all bullets behind ship and aliens
  for bullet in bullets.sprites(): # why iterate over bullets.sprites() if just bullets work??
    bullet.draw_bullet()

  ship.blitme()
  aliens.draw(screen)

  # make the most recently drawn screen visible
  pygame.display.flip()

def update_bullets(bullets):
  """Update position of bullets and get rid of old bullets"""
  # update position
  bullets.update()

  # get rid of bullets that have disappeared
  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)

def create_fleet(fi_settings, screen, aliens):
  """Create full fleet of aliens"""
  # create an alien and find the number of aliens in a row
  # spacing between aliens is equal to one alien width
  alien = Alien(fi_settings, screen)
  alien_width = alien.rect.width
  available_space_x = fi_settings.screen_width - 2 * alien_width
  number_aliens_x = int(available_space_x / (2 * alien_width))

  # create first row of aliens
  for alien_number in range(number_aliens_x):
    # create alien and place it in the row
    alien = Alien(fi_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)