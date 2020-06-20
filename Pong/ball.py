import config
import pygame as pg

class Ball(pg.sprite.Sprite):
  def __init__(self, color, radius):
    super().__init__()

    self.image = pg.Surface([radius * 2, radius * 2])
    self.image.fill(config.BLACK)
    self.image.set_colorkey(config.BLACK)

    pg.draw.circle(self.image, color, (int(self.image.get_width()/2), int(self.image.get_height()/2)), radius)
    self.rect = self.image.get_rect()

    self.velocity = [3, 3]

  def changeDirection(self):
    self.velocity[0] = -self.velocity[0]

  def update(self):
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]

  def velUp(self):
    if self.velocity[0] > 0:
      self.velocity[0] += 1
    else:
      self.velocity[0] -= 1