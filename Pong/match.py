import config
import pygame as pg
from player import *
from ball import *

score_space = pg.Surface((config.SCREEN_WIDTH, int(config.SCREEN_HEIGHT / 10)))
score_space_rect = score_space.get_rect()
field_space = pg.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT - score_space.get_height()))
field_space_rect = field_space.get_rect()

ball = Ball(config.WHITE, config.BALL_RADIUS)
ball.rect.x, ball.rect.y = (config.SCREEN_WIDTH / 2 - config.BALL_RADIUS / 2), (config.SCREEN_HEIGHT / 2  - config.BALL_RADIUS / 2 + score_space_rect.bottom)

player1 = Player(config.WHITE, config.PLAYER_WIDTH, config.PLAYER_HEIGHT, score_space_rect.bottom)
player1.rect.x, player1.rect.y = 20, (config.SCREEN_HEIGHT / 2 - config.PLAYER_HEIGHT / 2)
player2 = Player(config.WHITE, config.PLAYER_WIDTH, config.PLAYER_HEIGHT, score_space_rect.bottom)
player2.rect.x, player2.rect.y = (config.SCREEN_WIDTH - config.PLAYER_WIDTH - 20), (config.SCREEN_HEIGHT / 2 - config.PLAYER_HEIGHT / 2)

sprites_group = pg.sprite.Group()
sprites_group.add(player1)
sprites_group.add(player2)
sprites_group.add(ball)

reset_ball = 0
last_vel = 0

def show():
  global reset_ball, last_vel
  
  if config.mode == 0:
    if config.score1 == config.max_points:
      config.winner = "Player 1"
      config.match = False
      config.final = True
    elif config.score2 == config.max_points:
      config.winner = "Player 2"
      config.match = False
      config.final = True
  elif config.mode == 1:
    if config.score1 > config.score2:
      config.winner = "Player 1"
    elif config.score2 > config.score1:
      config.winner = "Player 2"
    else:
      config.winner = "Empate"
  elif config.mode == 2:
    if pg.time.get_ticks() > last_vel + 10000:
      ball.velUp()
      last_vel = pg.time.get_ticks()
    if config.score1 > config.score2:
      config.winner = "Player 1"
      config.match = False
      config.final = True
    elif config.score2 > config.score1:
      config.winner = "Player 2"
      config.match = False
      config.final = True

  if reset_ball != 0:
    delay_time = pg.time.get_ticks()
    pg.time.delay(1000)
    delay_time = pg.time.get_ticks() - delay_time
    config.duration += delay_time / 1000
    ball.rect.x, ball.rect.y = (config.SCREEN_WIDTH / 2), (config.SCREEN_HEIGHT / 2 + score_space_rect.bottom)
    reset_ball = 0

  pressed = pg.key.get_pressed()
  if pressed[pg.K_w]:
    player1.moveUp(5)
  if pressed[pg.K_s]:
    player1.moveDown(5)
  if pressed[pg.K_UP]:
    player2.moveUp(5)
  if pressed[pg.K_DOWN]:
    player2.moveDown(5)

  if ball.rect.x >= (config.SCREEN_WIDTH - config.BALL_RADIUS):
    config.score1 += 1
    reset_ball = 1
    ball.velocity[0] = -ball.velocity[0]
  if ball.rect.x<=0:
    config.score2 += 1
    reset_ball = 2
    ball.velocity[0] = -ball.velocity[0]
  if ball.rect.y >= (config.SCREEN_HEIGHT - config.BALL_RADIUS):
    ball.velocity[1] = -ball.velocity[1]
  if ball.rect.y < score_space_rect.bottom:
    ball.velocity[1] = -ball.velocity[1] 

  if pg.sprite.collide_mask(ball, player1) or pg.sprite.collide_mask(ball, player2):
    ball.changeDirection()

  sprites_group.update()
  pg.draw.line(config.screen, config.WHITE, [config.SCREEN_WIDTH / 2 - 2.5, score_space_rect.bottom], [config.SCREEN_WIDTH/2 - 2.5, config.SCREEN_HEIGHT], 5)
  pg.draw.rect(config.screen, config.WHITE, score_space_rect, 5)
  sprites_group.draw(config.screen)

  font = pg.font.Font(None, 74)
  text = font.render(str(config.score1), 1, config.WHITE)
  config.screen.blit(text, (config.SCREEN_WIDTH / 4 - text.get_rect().width / 2, (score_space_rect.bottom / 2 - text.get_rect().height / 2)))
  
  if config.mode == 1:
    font = pg.font.Font(None, 100)
    text = font.render(str("%2.2f" % config.duration), 1, config.WHITE)
    config.screen.blit(text, (config.SCREEN_WIDTH / 2 - text.get_rect().width / 2, (score_space_rect.bottom / 2 - text.get_rect().height / 2)))
  
  font = pg.font.Font(None, 74)
  text = font.render(str(config.score2), 1, config.WHITE)
  config.screen.blit(text, (config.SCREEN_WIDTH - config.SCREEN_WIDTH / 4 - text.get_rect().width / 2, (score_space_rect.bottom / 2 - text.get_rect().height / 2)))