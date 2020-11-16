from getpass import*
import pygame
import random

# Assesment started on 3-11-20 and finished on 10-11-20
pygame.init()
rand_artist = ["Teejay Wynn","Romy Salazar","Blade Mata","Luther Gilmour","Denise Willis"]
rand_songs = ["melon chords","pointy ants","snoozy tom","my time","crazy map"]
random.shuffle(rand_artist)
random.shuffle(rand_songs)

username = str(input("Enter your name: "))
if len(username) > 6:
    raise ValueError("Invalid username length")

password = getpass("Enter your password: ")


def manage_file():
    with open('songs', 'w') as s:
        for i in range(len(rand_artist)):
            s.write("Artist " + str(i + 1) + " = " + rand_artist[i] + "\n" + rand_songs[
                i] + "\n")


def store_personal_stuff(a, b):
    with open('info', 'w') as info:
        info.write("Username = " + a)
        info.write("\nPassword = " + b)


store_personal_stuff(username, password)
manage_file()
PATH = r'C:\Users\arnau\Pictures\Saved Pictures'
image = pygame.image.load(PATH + '\music.png.png')
FPS = 60
clock = pygame.time.Clock()
WIDTH, HEIGHT = 700, 650
WHITE = 255, 255, 255
BLACK = 0, 0, 0
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music player")
FONT = pygame.font.SysFont('comicsans', 32)
txt = FONT.render("Hi " + username[0].upper() + str(username[1:]) + "! Are you ready to take this Quiz?", True, (255, 0, 0))
make_a_guess_txt = "Your guess: "
score_list = []
t = ""

expand_x = 50
expand_y = 500
score = 0
indexer = random.randint(0, len(rand_artist) - 1)
inpt = ""
score = 0
atts = 3
seed = (indexer * 2) + 1


if len(inpt) > 19:
    raise ValueError("Max length exceeded")

run = True

while run:
    correct = False
    WIN.fill(WHITE)
    clock.tick(FPS)
    find = int((rand_songs[indexer].find(" ")) + 1)
    artist = FONT.render("Random artist\'s name = " + rand_artist[indexer], True, BLACK)
    song = "Random song\'s name = " + rand_songs[indexer][0] + " ... " + rand_songs[indexer][find]
    k = random.randint(1, len(inpt) + 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                inpt = inpt[:-1]
                expand_x -= 12.5
            else:
                inpt += event.unicode
                expand_x += 12.5

        if inpt == rand_songs[indexer]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    correct = True
                else:
                    correct = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if inpt != rand_songs[indexer]:
                    nt_qt = FONT.render("Not quite...", True, BLACK)
                    WIN.blit(nt_qt, (10, 550))
                    atts -= 1
                    inpt = ""
                    correct = False
                    expand_x = 50
                    expand_y = 500

        if not correct:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if inpt != rand_songs[indexer]:
                        score += 1


    if atts <= 0:
        lost = FONT.render("You lost...", True, BLACK)
        WIN.blit(lost, (270, 325))
        run = False
        print("GAME OVER!!!")

    if correct:
        score += 3
        right = FONT.render("You Are right!!", True, (255, 0, 0))
        WIN.blit(right, (10, 570))
        indexer = random.randint(0, len(rand_artist) - 1)

    rnd_score = FONT.render("Score = " + str(score), True, BLACK)
    if expand_x <= 50:
        expand_x = 50
    if expand_y <= 500:
        expand_y = 500
    pygame.draw.line(WIN, BLACK, (0, 420), (expand_x, 420), 3)
    pygame.draw.line(WIN, BLACK, (expand_x, 420), (expand_x, expand_y), 3)
    pygame.draw.line(WIN, BLACK, (0, 500), (expand_x, expand_y), 3)
    WIN.blit(txt, (10, 10))
    WIN.blit(rnd_score, (550, 570))
    surface_atts = FONT.render("Attempts = " + str(atts), True, BLACK)
    WIN.blit(surface_atts, (550, 590))
    WIN.blit(artist, (10, 150))
    surface_song = FONT.render(song, True, BLACK)
    surface_input = FONT.render(inpt, True, BLACK)
    surface_guess = FONT.render(make_a_guess_txt, True, BLACK)
    WIN.blit(surface_song, (10, 250))
    WIN.blit(surface_input, (10, 450))
    WIN.blit(surface_guess, (0, 390))
    WIN.blit(image, (550, 10))
    pygame.display.update()
pygame.quit()
