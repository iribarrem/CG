import pygame as pg
import time

pg.init()

BLACK, WHITE = (0, 0, 0), (255, 255, 255)

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pg.display.set_mode(SCREEN_SIZE)
screen_rect = screen.get_rect()

width, height = 50, 50
square = pg.Surface((width, height))
positive_scale = True

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()

  if width == SCREEN_WIDTH:
    positive_scale = False
  elif width == 1:
    positive_scale = True

  if positive_scale:
    width += 1
    height += 1
  else:
    width -= 1
    height -= 1

  screen.fill(BLACK)
  
  square = pg.transform.scale(square, (width, height))
  square.fill(WHITE)
  square_position = ((SCREEN_WIDTH/2 - width/2), (SCREEN_HEIGHT/2 - width/2))
  screen.blit(square, square_position)

  pg.display.update()
  pg.time.delay(5)
  
pg.quit()


