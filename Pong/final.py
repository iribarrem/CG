import config
import pygame as pg

def show():
  font = pg.font.Font(None, 100)
  text = font.render(str("Vencedor"), 1, config.WHITE)
  config.screen.blit(text, (config.SCREEN_WIDTH / 2 - text.get_rect().width / 2, (config.SCREEN_HEIGHT / 4 - text.get_rect().height / 2)))

  font = pg.font.Font(None, 250)
  text = font.render(str(config.winner), 1, config.WHITE)
  config.screen.blit(text, (config.SCREEN_WIDTH / 2 - text.get_rect().width / 2, (config.SCREEN_HEIGHT / 4 + 200 - text.get_rect().height / 2)))

  font = pg.font.Font(None, 50)
  text = font.render(str("Reiniciar"), 1, config.WHITE)
  font.set_underline(True)
  config.screen.blit(text, (config.SCREEN_WIDTH / 2 - text.get_rect().width / 2, (config.SCREEN_HEIGHT / 4 + 400 - text.get_rect().height / 2)))

  for event in pg.event.get():
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_SPACE:
        config.score1 = 0
        config.score2 = 0
        config.duration = 10
        config.menu = True
        config.final = False
        config.start = True