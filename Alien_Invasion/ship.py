import pygame

class Ship():

  def __init__(self,screen):
    self.screen = screen
    self.image = pygame.image.load('images/spaceship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    #movement flag
    self.moving_right = False

  def update(self):
    #update ship's position based on the movement flag
    if self.moving_right:
      self.rect.centerx += 1

  def blitme(self):
    #"draw ship at its current location"
    self.screen.blit(self.image, self.rect)

    