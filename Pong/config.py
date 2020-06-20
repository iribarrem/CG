import pygame as pg

BLACK, WHITE = (0, 0, 0) , (255, 255, 255)
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pg.display.set_mode(screen_size)

BALL_RADIUS = 10
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 150

winner = 0
max_points = 1
duration = 10
mode = 0
mode_list = ["Pontos", "Tempo", "Ponto de Ouro"]
score1, score2 = 0, 0

menu = True
match = False
final = False
start = True

clock = pg.time.Clock()