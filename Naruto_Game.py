from tkinter.tix import Tree
from turtle import distance
import pygame
import random
import math
from pygame import mixer

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('bg.png')
#Background Music


#Caption and Icon
pygame.display.set_caption("Naruto")
icon = pygame.image.load('sasuke.png')
pygame.display.set_icon(icon)

#Creating a player
playerImg = pygame.image.load('naruto.png')
playerX = 100
playerY = 300
playerX_change = 0
playerY_change = 0
#ENEMY
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ninja.png'))
    enemyX.append(random.randint(400,700))
    enemyY.append(random.randint(0,500))
    enemyX_change.append(-30)
    enemyY_change.append(0.3)

#Rasengan
bulletImg = pygame.image.load('rasengan.png')
bulletX = 100
bulletY = 300
bulletX_change = 1
bulletY_change = 0
bullet_state = "ready"


# Score

score_value = 0
font = pygame.font.Font('naruto.ttf', 32)
over_font = pygame.font.Font('naruto.ttf', 64)

textX = 10
textY = 10

def player(x,y):
    screen.blit(pygame.transform.flip(playerImg, True, False),(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def bullet(x,y):
    global bullet_state
    bullet_state= "fire"
    screen.blit(bulletImg,(x+16,y+16))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
def isDead(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
    if distance < 20:
        return True
    else:
        return False

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


#Game Loop
def Naruto():
    global playerX,playerX_change,playerY,playerY_change,enemyX,enemyX_change,enemyY,enemyY_change,bulletX,bulletX_change,bulletY,bulletY_change,bullet_state,score_value
    running = True
    while running:
        

        screen.fill((0,0,0))
        #Background
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #KEYBOARD INPUT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    playerX_change = -0.9
                if event.key == pygame.K_d:
                    playerX_change = 0.9
                if event.key == pygame.K_w:
                        playerY_change = -0.9
                if event.key == pygame.K_s:
                    playerY_change = 0.9
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                         bullet_sound =mixer.Sound('Rasengan.mp3')
                         bullet_sound.play()   
                         bulletX = playerX
                         bulletY = playerY
                         bullet(bulletX,bulletY)

            if event.type== pygame.KEYUP:
                playerX_change = 0
                playerY_change = 0

        playerX += playerX_change
        playerY += playerY_change
        for i in range(num_of_enemies):
            enemyY[i] += enemyY_change[i]

        #Border Check
        if(playerX<0):
            playerX = 0
        elif playerX > 736:
            playerX = 736
        if(playerY<0):
                playerY = 0
        elif playerY > 536:
            playerY = 536

         #Border Check for enemy
        for i in range(num_of_enemies):
            dead = isDead(enemyX[i],enemyY[i],playerX,playerY)
            if dead:
                for j in range(num_of_enemies):
                    enemyX = 2000
                game_over()
                break
            if(enemyX[i]<0):
                enemyX_change[i] = 0.3
            elif enemyX[i] > 736:
                enemyX_change[i] = 0.3
            if(enemyY[i]<0):
                enemyY_change[i] = 0.3
                enemyX[i] += enemyX_change[i]
            elif enemyY[i]> 536:
                 enemyY_change[i] = -0.3
                 enemyX[i] += enemyX_change[i]

            collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
            if collision:
                explosion_sound = mixer.Sound('explosion.wav')
                explosion_sound.play()
                bulletX=100
                bulletY=300
                bullet_state="ready"
                score_value +=1
                enemyX[i] = random.randint(400,700)
                enemyY[i] = random.randint(0,500)
            enemy(enemyX[i], enemyY[i], i)

        #Bullet movement
        if bulletX > 780:
           bullet_state="ready"

        if bullet_state == "fire":
           bullet(bulletX,bulletY)
           bulletX += bulletX_change

    
    
        show_score(textX,textY)
        player(playerX,playerY)
        pygame.display.update()

