import pygame as pg
import config
import menu
import match
import final

pg.init()

pg.display.set_caption("Pong")

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()

  config.screen.fill(config.BLACK)

  if config.menu:
    menu.show()
  if config.match:
    if config.start:
      config.screen.fill(config.BLACK)
    if config.mode == 1:
      config.duration -= config.clock.get_time() / 1000
    match.show()
  if config.final:
    final.show()

  if config.duration <= 0:
    config.match = False
    config.final = True
  
  pg.display.flip()
  config.clock.tick(120)

  if config.start and config.match:
    delay_time = pg.time.get_ticks()
    pg.time.delay(1000)
    delay_time = pg.time.get_ticks() - delay_time
    config.duration += delay_time / 1000
    config.start = False