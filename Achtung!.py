"""
Importing everything I need for the program
"""
import pygame
from pygame.locals import *
import math
import random
pygame.init()
pygame.display.set_caption("Achtung! Feuer!")
#Create a surface object
screen = pygame.display.set_mode((1080, 600))

"""
Upload all the images and music
"""
icon = pygame.image.load("icon.png")
#set the icon
pygame.display.set_icon(icon)
#hitbox
hitbox = pygame.image.load("hitbox.png")
#characters
tanya = pygame.image.load("tanya.png")
sans = pygame.image.load("sans.png")
#weapons and bullets
bonebullet = pygame.image.load("bonebullet.png")
heart = pygame.image.load("heart.png")
blasteropen = pygame.image.load("blasteropen.png")
blasterclose = pygame.image.load("blasterclose.png")
blasterlaser = pygame.image.load("blasterlaser.png")
#Music
"""
megalovania = pygame.mixer.Sound("music/Megalovania.wav")
megalovania.set_volume(0.25)
"""
#startscreen and buttons
startscreen = pygame.image.load("startscreen.png")
start = pygame.image.load("start.png")
exitbutton = pygame.image.load("exitbutton.png")
rules = pygame.image.load("rules.png")
#choose characters
choosesans = pygame.image.load("choosesans.png")
choosetanya = pygame.image.load("choosetanya.png")
yes = pygame.image.load("yes.png")
goback = pygame.image.load("goback.png")

battlebackground = pygame.image.load("battlebackground.png").convert()
#storypages
storypage1 = pygame.image.load("storypage/storypage1.png")
storypage2 = pygame.image.load("storypage/storypage2.png")
storypage3 = pygame.image.load("storypage/storypage3.png")
storypage4 = pygame.image.load("storypage/storypage4.png")

#BOSS
bossv = pygame.image.load("bossv.png")
bosss = pygame.image.load("bosss.png")
bosshitbox = pygame.image.load("bosshitbox.png")
bulletinrow = pygame.image.load("bulletinrow.png")
#Class for the hitbox
class player():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self,screen):
        screen.blit(hitbox,(self.x,self.y))


def RedrawGameWindow():
    screen.blit(battlebackground,(0,0))








"""
#Make a hit box to represent the hit
def storydisplay():
    for i in range(300):
        screen.blit(storypage1,(0,0))
    for i in range(300):
        screen.blit(storypage2,(0,0))
    for i in range(300):
        screen.blit(storypage3,(0,0))
    for i in range(300):
        screen.blit(storypage4,(0,0))
"""          
def movecharacter(character):
    screen.blit(character,(x-25,y-60))

"""
Here are the bullet patterns form teh easiest to the hardest
"""


def circleofsqaures():
    pass








#shoots rows of sqaure bullets but with a random space in the rows for the character to pass
#the vel controls the speed of this bullet pattern

#this for loop the 11 random bullet positions into a list
def randomnuminlist(randomnumber):
    posofbullets = []
    for i in range(12):
        if i == randomnumber:
            pass
        else:
            posofbullets.append([1030,i*50])
    return posofbullets


#the random is used to determine where is the space, it's only used once, then there is another random num in the loop
randomnumforattack2 = random.randint(0,11)
posofbullets = randomnuminlist(randomnumforattack2)


def rowofbulletswithrandomspace(posofbullets,hitboxcol,vel):
    ifhit = [False,False]
    for i in range(11):
        posofbullets[i][0] -= vel
        rowcol = pygame.Rect(bulletinrow.get_rect())
        rowcol.x = posofbullets[i][0]
        rowcol.y = posofbullets[i][1]
        screen.blit(bulletinrow,posofbullets[i])
        if rowcol.colliderect(hitboxcol):
            ifhit[0] = True
        if posofbullets[i][0] < 0:
            ifhit[1] = True
    return ifhit

def randomflys():
    #The strategy is to stay in the middle of the screen and move around
    #random things will appear at all sides of the screen and move towards the two ends of the boss's wings
    pass
def rondombombing():
    #The 
    pass


 
mainloop = True
#Selection screen
mainScreen = True
#play screen
playScreen = True
attack = False
keys = [False,False,False,False]
#The original position of the player
x = 0
y = 200






"""
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
"""
#Speed of character
velocityofcharacter = 1.6
#The three lives
live1 = True
live2 = True
live3 = True
#if the space key is pressed the stat is true
shootbullets = False
#lits of bullets
bulletlist = []
#The invincibility protector
incinvible = 0
testnumber = 0
while mainloop:
    while mainScreen:
    #Start screen
        for event in pygame.event.get(): 
            screen.blit(startscreen,(0,0))
            screen.blit(start,(465, 230))
            screen.blit(rules,(465, 300))
            screen.blit(exitbutton,(465, 370))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex,mousey = pygame.mouse.get_pos()
                #First check the x value of the mouse, then the y values
                if mousex >= 465 and mousex <= 615:
                    #start the game, it will display the story and
                    #allow player to choose their character
                    if mousey >= 230 and mousey <= 280:
                        
                        mainScreen = False
                        mainLoop = True
                    #rules
                    if mousey >= 300 and mousey <= 350:
                        #Display "how to play this game: "
                        storydisplay()

                        
                    #exit
                    if mousey >= 370 and mousey <= 420:
                        mainScreen = False
                        playScreen = False
                        mainLoop = False

    while playScreen:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
                playScreen = False
            if event.type == pygame.KEYDOWN:
                if event.key==K_w:
                    keys[0]=True
                elif event.key==K_a:
                    keys[1]=True
                elif event.key==K_s:
                    keys[2]=True
                elif event.key==K_d:
                    keys[3]=True
                elif event.key==K_SPACE:
                    shootbullets = True
                elif event.key==K_ESCAPE:
                    pause == True
                elif event.key==K_RSHIFT or event.key==K_LSHIFT:
                    velocityofcharacter = 0.7
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    keys[0]=False
                elif event.key==pygame.K_a:
                    keys[1]=False
                elif event.key==pygame.K_s:
                    keys[2]=False
                elif event.key==pygame.K_d:
                    keys[3]=False
                elif event.key==K_SPACE:
                    shootbullets = False
                elif event.key==K_RSHIFT or event.key==K_LSHIFT:
                    velocityofcharacter = 1.6
        if keys[0] and y > 0:
            y -= velocityofcharacter
        elif keys[2] and y < 570:
            y += velocityofcharacter
        if keys[1] and x > 0:
            x -= velocityofcharacter
        elif keys[3] and x < 900:
            x += velocityofcharacter

        """
        print(hitboxcol.x)
        print(hitboxcol.y)
        print(testobject.x)
        print(testobject.y)
        """

        """
            for bullet in bulletlist:
                index=0
                velx=math.cos(bullet[0])*10
                vely=math.sin(bullet[0])*10
                bullet[1]+=velx
                bullet[2]+=vely
                if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
                    arrows.pop(index)
                index+=1
                for projectile in arrows:
                    arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
                    screen.blit(arrow1, (projectile[1], projectile[2]))
        """

        #The hitbox
        ###########very important########################
        hitboxcol = pygame.Rect(hitbox.get_rect())
        hitboxcol.x = x
        hitboxcol.y = y
        #################################################
        #The boss hitbox
        bosshitboxcol = pygame.Rect(bosshitbox.get_rect())
        bosshitboxcol.x = 900
        bosshitboxcol.y = 200
        """
        the live thing
        if hitboxcol.colliderect(testobject):
            live3 = False
        if live3 == False and hitboxcol.colliderect(testobject):
            live2 = False
        if live3 == False and live2 == False and hitboxcol.colliderect(testobject):
            live1 = False
        """
        screen.blit(battlebackground,(0,0))
        screen.blit(bossv,(880,0))
        screen.blit(bosshitbox,(900,200))
        
        if shootbullets == True and pygame.time.get_ticks()%100 == 0:
            bulletlist.append([x,y])

        index = 0
        for eachbullet in bulletlist:
            eachbullet[0] += 10
            bulletcol = pygame.Rect(bonebullet.get_rect())
            bulletcol.x = eachbullet[0]
            bulletcol.y = eachbullet[1]
            screen.blit(bonebullet,eachbullet)
            if bulletcol.colliderect(bosshitboxcol):
                testnumber += 1
                bulletlist.pop(index)
            if eachbullet[0]>1000:
                bulletlist.pop(0)
            index += 1



        

        movecharacter(sans)
        screen.blit(hitbox,(x,y))
        rowofbulletswithrandomspace(posofbullets,hitboxcol,0.7)
        if rowofbulletswithrandomspace(posofbullets,hitboxcol,0.7) == [True,False]:
            live3 = False
        elif rowofbulletswithrandomspace(posofbullets,hitboxcol,0.7) == [True,True]:
            for i in range(11):
                randomnumber = random.randint(0,11)
                posofbullets.pop(0)
            posofbullets = randomnuminlist(randomnumber)
        elif rowofbulletswithrandomspace(posofbullets,hitboxcol,0.7) == [False,True]:
            for i in range(11):
                randomnumber = random.randint(0,11)
                posofbullets.pop(0)
            posofbullets = randomnuminlist(randomnumber)


        
        if live1:
            screen.blit(heart,(0,0))
        if live2:
            screen.blit(heart,(40,0))
        if live3:
            screen.blit(heart,(80,0))
        pygame.display.update()

print(testnumber)
pygame.quit()

