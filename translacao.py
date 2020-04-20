import pygame as pg
import time

pg.init()

black, white = (0, 0, 0), (255, 255, 255)

screen_size = width, height = 600, 600
screen = pg.display.set_mode(screen_size)
screen_rect = screen.get_rect()

square_width, square_height = 50, 50
square = pg.Rect(275, 275, square_width, square_height)

delay = int(100 / (width / square_width))

def update():
  pg.time.delay(delay)
  screen.fill(black)
  square.clamp_ip(screen_rect)
  pg.draw.rect(screen, white, square)
  pg.display.update()

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()

  while square.right < width:
    square.move_ip(5, 0)
    update()
  while square.left > 0:
    square.move_ip(-5, 0)
    update()
  while square.right != 325:
    square.move_ip(5, 0)
    update()

  while square.top > 0:
    square.move_ip(0, -5)
    update()
  while square.bottom < height:
    square.move_ip(0, 5)
    update()
  while square.bottom != 325:
    square.move_ip(0, -5)
    update()