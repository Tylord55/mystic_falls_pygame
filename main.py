import pygame

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((600,600))

background = pygame.image.load('background.png')
#set screen caption
pygame.display.set_caption("Mystic Falls")

#window icon
#icon = pygame.image.load('vampire.png')
#display icon
#pygame.display.set_icon(icon)
#comment test

playerImg = pygame.transform.scale(pygame.image.load('damon.png'), (75, 115))
#playerImg = pygame.transform.scale(playerImg, (100, 100))
playerX = 350
playerY = 400
playerX_change = 0
playerY_change = 0
player_form = 1

elenaImg = pygame.transform.scale(pygame.image.load('elena.png'), (75, 115))
elenaX = 350
elenaY = 400
elenaImgX_change = 0
elenaImgY_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

def elena(x,y):
    screen.blit(elenaImg, (x,y))


running = True
while running:
    screen.fill((0,0,255))
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5
            if event.key == pygame.K_t:
                if(player_form == 1):
                    playerImg = pygame.transform.scale(pygame.image.load('stefan.png'), (75, 115))
                    player_form = 0
                else:
                    playerImg = pygame.transform.scale(pygame.image.load('damon.png'), (75, 115))
                    player_form = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
        #if event.type == pygame.KEYUP:
            #if event.key == pygame.K_t:
                #playerImg = pygame.transform.scale(pygame.image.load('damon.png'), (75, 115))



    
    player(playerX, playerY)
    elena(elenaX, elenaY)

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 525:
        playerX = 525

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 500:
        playerY = 500

    #update the screen
    pygame.display.update()
