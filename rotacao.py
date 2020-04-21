import pygame as pg
import time

pg.init()

BLACK, WHITE = (0, 0, 0), (255, 255, 255)

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pg.display.set_mode(SCREEN_SIZE)
screen_rect = screen.get_rect()

width, height = 50, 100
square = pg.Surface((width, height), pg.SRCALPHA)
angle = 0

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()

  screen.fill(BLACK)

  square = pg.transform.rotate(square, angle)
  square.fill(WHITE)
  if angle < 360:
    angle += 1
  else:
    angle = 0
    
  square_rect = square.get_rect(center=(0, 0))
  screen.blit(square, (square_rect.x + 300, square_rect.y + 300))

  pg.display.update()
  pg.time.delay(1000)
  
pg.quit()