import config
import pygame as pg

class Player(pg.sprite.Sprite):
  def __init__(self, color, width, height, field_top):
    super().__init__()
    self.height = height
    self.field_top = field_top

    self.image = pg.Surface([width, height])
    self.image.fill(config.BLACK)
    self.image.set_colorkey(config.BLACK)

    pg.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()

  def moveDown(self, distance):
    self.rect.y += distance
    if self.rect.y > (config.SCREEN_HEIGHT - self.height):
      self.rect.y = (config.SCREEN_HEIGHT - self.height)

  def moveUp(self, distance):
    self.rect.y -= distance
    if self.rect.y < self.field_top:
      self.rect.y = self.field_top