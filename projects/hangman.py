# Inspired by YT: Tech With Tim

import math
import pygame

pygame.init()

# Setting main variables and decoration

SECRET_WORD = str()
ATTEMPTS = int()

WIDTH, HEIGHT = 750, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman w/ pygame - ArnauCodes')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
clock = pygame.time.Clock()

images = []
chars = []


curr_hangman = 0

# 9 images in total

for i in range(9):
	image = pygame.image.load("Hangman" + str(i) + ".png")
	images.append(image)


# Decoded ASCII values

for i in range(65, 91):
	chars.append(chr(i))

FONT = pygame.font.SysFont('comicsans', 40)

RADIUS = 20

circlex, circley = 70, 530

def draw(x, y):
	WIN.fill(WHITE)
	for letter in range(26):
		pygame.draw.circle(WIN, BLACK, (x, y), RADIUS , 3)
		txt = FONT.render(chars[letter], 1, BLACK)
		WIN.blit(txt, (x - 10, y - 12))
		x += 50
		if letter == 12:
			x = circlex
			y += 55
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				x_dis = pygame.mouse.get_pos()
				'''dis = math.sqrt((x - x_dis)**2 + (y - y_dis)**2)
				if dis <= RADIUS:
					pass'''
				print(x_dis)
					


	WIN.blit(images[curr_hangman], (420, 130))
	pygame.display.update()
		


# Main game loop

run = True

while run:
	clock.tick(FPS)
	draw(circlex, circley)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	
			pygame.quit()
pygame.quit()
