import pygame

# pygame 'starten'
pygame.init()

# variabelen
screen_width, screen_height = 640, 400

black = (0, 0, 0)
white = (255, 255, 255)

jump = False
duck = False
jumped = 0
height = 100

dino_x = screen_width * 0.15
dino_y = screen_height * 0.65
dinoVelY = 0

# titel
pygame.display.set_caption('Jumpy')
# klok
clock = pygame.time.Clock()
# scherm maken
screen = pygame.display.set_mode((screen_width, screen_height))

# dino laden
dinoImg = pygame.image.load('img\Player.png')


# functies
def dino(dino_x, dino_y):
    screen.blit(dinoImg, (dino_x, dino_y))

# voorwaarden loop
death = False

# loop
while not death:
    # alle inputs opvragen
    for event in pygame.event.get():
        # afhandelen van sluiten van de game
        if event.type == pygame.QUIT:
            # uit loop komen
            death = True

        # inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                death = True
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and not jump:
                jump = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                duck = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                death = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                jump = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                duck = False

    if jump:
        jumped += 8
        if jumped >= height:
            jump = False
    elif jumped > 0 and not jump:
        jumped -= 8

    screen.fill(white)

    dino(dino_x, dino_y - jumped)

    # alles updaten (framesgewijs)
    pygame.display.update()

    # fps
    clock.tick(60)


# afsluiten
pygame.quit()
quit()
