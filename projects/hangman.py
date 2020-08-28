# Inspired by YT: Tech With Tim

import pygame, getpass

pygame.init()

# Constraints
def quit():
  pygame.quit()

print("\n\nPlayer 1, chooses the word\nPlayer 2, makes a guess\n\n")
SECRET_WORD = getpass.getpass(prompt="Player 1, Choose the word: ").lower()

# Make any number of hints(max is length of SECRET_WORD - 1)
hints = int(2)
if hints >= len(SECRET_WORD) - 1:
  hints = len(SECRET_WORD) - 1

# You must insert your final guess to see if it matches
final_guess = "".lower()

if len(SECRET_WORD) < 2 or len(SECRET_WORD) > 9:
  print("Secret word length must be > 1 and < 10")
  quit()

def create_constraint(s, e):
  for i in range(s, e):
    if chr(i) in SECRET_WORD:
      print("Only alphabetical values are allowed")
      quit()

# Non acceptable ASCII characters to be used
create_constraint(33, 65)
create_constraint(91, 97)
create_constraint(123, 127)

# Setting main variables and decoration


WIDTH, HEIGHT = 750, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman w/ pygame - ArnauCodes')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SX, SY= 94, 375
EX, EY = 124, 375
FPS = 60
clock = pygame.time.Clock()

images = []
chars = []
ca = []


# 8 images in total

for i in range(9):
  image = pygame.image.load("Hangman" + str(i) + ".png")
  images.append(image)


# Decoded ASCII values

for i in range(97, 123):
  chars.append(chr(i))

FONT = pygame.font.SysFont('comicsans', 40)

RADIUS = 20

circlex, circley = 70, 530


def draw_line(sx, sy, ex, ey):
  pygame.draw.line(WIN, BLACK, (sx, sy), (ex, ey), 5)



def draw(x, y):
  WIN.fill(WHITE)
  for i in range(26):
    pygame.draw.circle(WIN, BLACK, (x, y), RADIUS , 3)
    txt = FONT.render(chars[i], 1, BLACK)
    WIN.blit(txt, (x - 7, y - 12))
    x += 50
    if i == 12:
      x = circlex
      y += 55







def choose_word(guess):
  global curr_hangman, guess_len, wrong_answers
  curr_hangman = 0
  guess_len = len(guess)
  if type(guess) != set:
    print("Place all your attempts in a set")
    quit()

  for i in guess:
    i.lower()
    if i in SECRET_WORD:
      ca.append(i)
      print(i, " is Correct!")
    else:
      print(i, " Nope..")
      curr_hangman += 1

  if len(list(SECRET_WORD)) != len(set(SECRET_WORD)):
    print("Hmmmm, there is probably a word that is repeated twice or more...\n")

  wrong_answers = abs(guess_len - len(ca))   

  
choose_word({"h", "i"})

u_lost_txt = FONT.render("You lost, the word was: " + SECRET_WORD, 1, BLACK)

# Main game loop
run = True

while run:
  clock.tick(FPS)
  draw(circlex, circley)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False	
      pygame.quit()
  stages = FONT.render("Hangman level: " + str(curr_hangman) + " / 8", 1, BLACK)
  rendered_good_ans = FONT.render("Correct answers " + str(len(ca)) + " / " + str(len(SECRET_WORD)), 1, BLACK)
  for i in range(hints):
    hint_txt = FONT.render("The word includes \'" + SECRET_WORD[i] + "\' in it", 1, BLACK)
  if final_guess == SECRET_WORD and wrong_answers < 8:
    u_won_txt = FONT.render("YOU WON! It was: " + SECRET_WORD, 1, BLACK)
    WIN.blit(u_won_txt, (50, HEIGHT // 2))
  if wrong_answers >= 8:
    WIN.blit(u_lost_txt, (50, HEIGHT // 2))
  WIN.blit(images[curr_hangman], (475, 250))
  WIN.blit(stages, (410 , HEIGHT // 4))
  WIN.blit(rendered_good_ans, (50, (HEIGHT * 2) // 3))
  WIN.blit(hint_txt, (WIDTH // 2, (HEIGHT * 2) // 3))

  pygame.display.update()
pygame.quit()
