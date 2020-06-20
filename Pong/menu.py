import config
import pygame as pg

sel = 0

def show():
  global sel

  font = pg.font.Font(None, 250)
  text = font.render(str("PONG"), 1, config.WHITE)
  config.screen.blit(text, (config.SCREEN_WIDTH / 2 - text.get_rect().width / 2, (config.SCREEN_HEIGHT / 4 - text.get_rect().height / 2)))

  string = "Modo de Jogo:  <  " + config.mode_list[config.mode] + "  >"
  font = pg.font.Font(None, 50)
  if sel == 0:
    font.set_underline(True)
  else:
    font.set_underline(False)
  text = font.render(string, 1, config.WHITE)
  config.screen.blit(text, (config.SCREEN_WIDTH / 2 - text.get_rect().width / 2, (config.SCREEN_HEIGHT / 2 - text.get_rect().height / 2)))

  if config.mode != 2:
    if config.mode == 0:
      string = "Número de Pontos:  <  " + str(config.max_points) + "  >"
    elif config.mode == 1:
      string = "Tempo:  <  " + str(config.duration) + "  >"
    font = pg.font.Font(None, 50)
    if sel == 1:
      font.set_underline(True)
    else:
      font.set_underline(False)
    text = font.render(string, 1, config.WHITE)
    config.screen.blit(text, (config.SCREEN_WIDTH / 2 - text.get_rect().width / 2, (config.SCREEN_HEIGHT / 2 + 50 - text.get_rect().height / 2)))

  string = "INICIAR"
  font = pg.font.Font(None, 50)
  if sel == 2:
    font.set_underline(True)
  else:
    font.set_underline(False)
  text = font.render(string, 1, config.WHITE)
  config.screen.blit(text, (config.SCREEN_WIDTH / 2 - text.get_rect().width / 2, (config.SCREEN_HEIGHT / 2 + 100 - text.get_rect().height / 2)))

  for event in pg.event.get():
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_DOWN:
        if sel >= 2:
          sel = 2
        else:
          sel += 1
      elif event.key == pg.K_UP:
        if sel <= 0:
          sel = 0
        else:
          sel -= 1
      elif event.key == pg.K_LEFT:
        if sel == 0:
          if config.mode <= 0:
            config.mode = 0
          else:
            config.mode -= 1
        elif sel == 1:
          if config.mode == 0:
            if config.max_points <= 1:
              config.max_points = 1
            else:
              config.max_points -= 1
          elif config.mode == 1:
            if config.duration <= 10:
              config.duration = 10
            else:
              config.duration -= 10
      elif event.key == pg.K_RIGHT:
        if sel == 0:
          if config.mode >= 2:
            config.mode = 2
          else:
            config.mode += 1
        elif sel == 1:
          if config.mode == 0:
            config.max_points += 1
          elif config.mode == 1:
            config.duration += 10
      elif event.key == pg.K_SPACE:
        if sel == 2:
          config.menu = False
          config.match = True