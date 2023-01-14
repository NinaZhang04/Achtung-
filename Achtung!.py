"""
Importing everything I need for the program
"""
import pygame
from pygame.locals import *
import math
import random
import sys
pygame.init()
pygame.display.set_caption("Achtung! Feuer!")
#Create a surface object
screen = pygame.display.set_mode((1080, 600))


"""
Upload all the images and music and initialize some values(defining variaebles)
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
vertlaser = pygame.image.load("vertlaser.png")
#Music
revolovania = pygame.mixer.Sound("music/revolovania.wav")
wahwahwah = pygame.mixer.Sound("music/wahwahwah.wav")
los = pygame.mixer.Sound("music/los.wav")
quietwater = pygame.mixer.Sound("music/quietwater.wav")
blastereffect = pygame.mixer.Sound("music/blastereffect.wav")
pygame.mixer.music.set_volume(0.5)

#blasters
blasterclose = pygame.image.load("blasterclose.png")
blasteropen = pygame.image.load("blasteropen.png")
blasterlaser = pygame.image.load("blasterlaser.png")
#startscreen and buttons
startscreen = pygame.image.load("startscreen.png")
start = pygame.image.load("start.png")
exitbutton = pygame.image.load("exitbutton.png")
rules = pygame.image.load("rules.png")
#choose characters
yes = pygame.image.load("yes.png")
goback = pygame.image.load("goback.png")
battlebackground = pygame.image.load("battlebackground.png").convert()
#storypages
storypage1 = pygame.image.load("storypage/storypage1.png").convert()
storypage2 = pygame.image.load("storypage/storypage2.png").convert()
storypage3 = pygame.image.load("storypage/storypage3.png").convert()
storypage4 = pygame.image.load("storypage/storypage4.png").convert()
selectionpage = pygame.image.load("storypage/selectionpage.png").convert()
rulepage = pygame.image.load("rulepage.png").convert()
#endings
badending = pygame.image.load("storypage/badending.png").convert()
normalending = pygame.image.load("storypage/normalending.png")
goodending = pygame.image.load("storypage/happyending.png").convert()
youdied = pygame.image.load("youdied.png")
#results
ss = pygame.image.load("ss.png")
s = pygame.image.load("s.png")
a = pygame.image.load("a.png")
b = pygame.image.load("b.png")
c = pygame.image.load("c.png")
d = pygame.image.load("d.png")
f = pygame.image.load("f.png")
#BOSS
oneblock = pygame.image.load("oneblock.png")
warning = pygame.image.load("warning.png")
bossv = pygame.image.load("bossv.png")
bosss = pygame.image.load("bosss.png")
bossk = pygame.image.load("bossk.png")
bosshitbox = pygame.image.load("bosshitbox.png")
bulletinrow = pygame.image.load("bulletinrow.png")
healthbar = pygame.image.load("healthbar.png")
healthbar2 = pygame.image.load("healthbar2.png")
healthbar3 = pygame.image.load("healthbar3.png")
healthbar4 = pygame.image.load("healthbar4.png")
healthbar5 = pygame.image.load("healthbar5.png")
healthbar6 = pygame.image.load("healthbar6.png")
masterloop = True
storyloop = True
while storyloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key ==K_a:
                storyloop = False
    if pygame.time.get_ticks() <= 4000:
        screen.blit(storypage1,(0,0))
    elif pygame.time.get_ticks() <= 7000:
        screen.blit(storypage2,(0,0))
    elif pygame.time.get_ticks() <= 12000:
        screen.blit(storypage3,(0,0))
    elif pygame.time.get_ticks() <= 15000:
        screen.blit(storypage4,(0,0))
    else:
        break
    pygame.display.update()


while masterloop:
    bosshealth = 1800
    #The invincibility protector
    invincible1 = 300
    shield1 = True
    invincible2 = 300
    shield2 = True
    #Speed of character
    velocityofcharacter = 2
    #The three lives
    live1 = True
    live2 = True
    live3 = True
    #if the space key is pressed the stat is true
    shootbullets = False
    #lits of bullets
    bulletlist = []
    #shots, hit and missed
    shots = 0
    hit = 0
    #if you loses all your health
    youdead = False
    died = 0
    badendingloop = False
    normalendingloop = False
    goodendingloop = False
    #choose character
    sansortanya = True
    #screens
    mainloop = True
    mainScreen = True
    playScreen = True
    results = True
    #keys
    keys = [False,False,False,False]
    #The original position of the player
    x = 500
    y = 200
    font = pygame.font.SysFont("System",30)
    #Judging the player's performance
    bossdead = False
    bossoverdead = False
    accuracy = 0
    #cheat mode setting!!!!!!
    #press C during the title screen can acticate the cheat mode
    cheat = False
    def RedrawGameWindow():
        screen.blit(battlebackground,(0,0))
    def movecharacter(character):
        screen.blit(character,(x-25,y-60))









    ################################bullet patterns#################################
    #
    #
    #
    #patteren1#########################################################################
    xvalue = [800]
    """
    get a random number. this is a seperate function so that in the while loop
    it only randomnizes after the condition is triggered. this randomize the y position
    of the big block
    """
    def randomshoot():
        randomnum = random.randint(100,400)#this causes the block to only blit
        #infront of the boss hitbox
        return randomnum
    """
    xvalue is the changable start position of the big block. It will only reset when
    the old block reaches the end of the screen. it is set as a list
    because of testing reasons, but after testing it seems unneccisary to change it
    back to a integer, so I just left it as a list
    """
    def onebigbullet(xvalue,randomnum,hitboxcol,speed):
        ifhit = [False,False]
        xvalue[0] -= speed
        oneblockcol = pygame.Rect(oneblock.get_rect())
        oneblockcol.x = xvalue[0]
        oneblockcol.y = randomnum
        screen.blit(oneblock,(xvalue[0],randomnum))
        if oneblockcol.colliderect(hitboxcol):
            ifhit[0] = True
        if xvalue[0] <= 0:
            ifhit[1] = True
        return ifhit
    onerandom = randomshoot()    
    tworandom = randomshoot()
    #################################################################################
    #
    #
    #
    #
    #Patteren 2#####################################################################
    """
    shoots rows of sqaure bullets but with a random space in the rows
    for the character to pass
    the vel controls the speed of this bullet pattern
    this for loop the 11 random bullet positions into a list
    """
    #the random number is defined in the while loop. It is defined again when the
    #old list of bullets are out of the screen
    def randomnuminlist(randomnumber):
        posofbullets = []
        for i in range(12):
            if i == randomnumber:
                pass
            else:
                posofbullets.append([1030,i*50])
        return posofbullets
    #the random numbers is used to determine where is the space
    randomnumforattack2 = random.randint(0,11) #This one is only used once,
    #then there is another random num in the loop
    posofbullets = randomnuminlist(randomnumforattack2)
    def rowofbulletswithrandomspace(posofbullets,hitboxcol,vel):
        """
        the ifhit is going to appear in most of the bullet patterens. The
        first item in the list determines if it hits the character, the second
        item in the list determines if the bullets reaches the end of the playscreen
        if it is, we start to pop the list and clear the list
        """
        ifhit = [False,False]
        for i in range(11):
            posofbullets[i][0] -= vel
            rowcol = pygame.Rect(bulletinrow.get_rect())
            rowcol.x = posofbullets[i][0]
            rowcol.y = posofbullets[i][1]
            screen.blit(bulletinrow,posofbullets[i])
            if rowcol.colliderect(hitboxcol):
                ifhit[0] = True
            if posofbullets[i][0] <= 0:
                ifhit[1] = True
        return ifhit
    #################################################################################
    #
    #
    #
    #
    #Patteren3#######################################################################
    #Randomlize the position of the flies and control
    #them to move towards one direction
    def appendflylist(flylist,bulletnum):
        for i in range(bulletnum):
            xpos = random.randint(-100,0)
            ypos = random.randint(-100,700)
            flylist.append([xpos,ypos])
    flylist1 = []
    appendflylist(flylist1,3)
    flylist2 = []
    appendflylist(flylist2,3)
    flylist3 = []
    appendflylist(flylist3,3)
    flylist4 = []
    appendflylist(flylist4,3)
    flylist5 = []
    appendflylist(flylist5,3)
    def clearflylist(flylist,bulletnum):
        for i in range(bulletnum):
            flylist.pop(0)
    def randomflys(hitboxcol,flylist,speed,position):
        #markmark
        ifhitfly = [False,False]
        for fly in flylist:
            posx=(position[0]-fly[0])*speed
            posy=(position[1]-fly[1])*speed
            fly[0]+=posx
            fly[1]+=posy
            flycol = pygame.Rect(bosss.get_rect())
            flycol.x = fly[0]
            flycol.y = fly[1]
            if flycol.colliderect(hitboxcol):
                ifhitfly[0] = True
            if fly[0]>= 950:
                ifhitfly[1] = True
            for projectile in flylist:
                screen.blit(bosss,(projectile[0], projectile[1]))
        return ifhitfly        
    ################################################################################
    #
    #
    #
    #
    #pattern 4#########################################################################
    bulletpos1 = [[800,300]]
    bulletpos2 = [[800,300]]
    bulletpos3 = [[800,300]]
    bulletpos4 = [[800,300]]
    bulletpos5 = [[800,300]]
    def createline(bulletpos,gametime,pos):
        if pygame.time.get_ticks()%300 >= 0 and pygame.time.get_ticks()%300 <= 5:
            bulletpos.append(pos)
        if bulletpos[0][0] <= 0 or bulletpos[0][1] <= 0 or bulletpos[0][1] >= 600:
            bulletpos.pop(0)
        return bulletpos

    def linehell(hitboxcol,bulletpos,pos):
        """
        hitboxcol is the hitbox, bulletpos is the current position that the bullet
        is at, the pos is a list. pos[0] is how much x value does it move, and pos[y]
        is how much y value it moves. I make "pos" a list instead of two numbers
        because I do not want to define anymore x's and y's. I already have a lot of
        variables in the game.
        """
        ifhit = False
        for bullet in bulletpos:
            bullet[0] += pos[0]
            bullet[1] += pos[1]
            bulletcol = pygame.Rect(bossk.get_rect())
            bulletcol.x = bullet[0]
            bulletcol.y = bullet[1]
            if bulletcol.colliderect(hitboxcol):
                ifhit = True
            screen.blit(bossk,(bullet[0],bullet[1]))
        return ifhit
    ################################################################################
    #
    #
    #
    #
    #Pattern5#######################################################################
    #Pattern 5 will be in the loop
    ################################################################################

    while mainloop:
        los.play()
        while mainScreen:
            rulepagedis = True
            screen.blit(startscreen,(0,0))
            screen.blit(start,(465, 230))
            screen.blit(rules,(465, 300))
            screen.blit(exitbutton,(465, 370))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex,mousey = pygame.mouse.get_pos()
                    #First check the x value of the mouse, then the y values
                    if mousex >= 465 and mousex <= 615:
                        #start the game, it will display the story and
                        #allow player to choose their character
                        if mousey >= 230 and mousey <= 280:
                            storydisplay = True
                            while storydisplay:
                                screen.blit(selectionpage,(0,0))
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key ==K_s:
                                            sansortanya = True#player choose sans
                                            storydisplay = False
                                        if event.key == K_t:
                                            sansortanya = False#player choose tanya
                                            storydisplay = False
                            while rulepagedis:
                                screen.blit(rulepage,(0,0))
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key ==K_a:
                                            rulepagedis = False
                                            playScreen = True
                            starttime = pygame.time.get_ticks()
                            mainScreen = False
                            mainloop = True
                        #rules
                        if mousey >= 300 and mousey <= 350:
                        #the mouse position
                        #Display "how to play this game: "
                            while rulepagedis:
                                screen.blit(rulepage,(0,0))
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()

                                    if event.type == pygame.KEYDOWN:
                                        if event.key ==K_a:
                                            rulepagedis = False
                                         
                        #exit
                        if mousey >= 370 and mousey <= 420:
                            pygame.quit()
                            sys.exit()

        los.stop()
        revolovania.play()
        if  mainScreen == False and playScreen == False and mainloop == False:
            revolovania.stop()
        while playScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                    mainScreen= False
                    playScreen = False
                    results = False
                    revolovania.stop()
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
                    elif event.key==K_c:
                        cheat = True
                    elif event.key==K_UP:
                        velocityofcharacter = 3
                        #the player will move faster when up button is pressed
                    elif event.key==K_DOWN:
                        velocityofcharacter = 1
                        #player will move slower when down button is pressed
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
                    elif event.key==K_UP or event.key==K_DOWN:
                        velocityofcharacter = 2
            if keys[0] and y > 0:
                y -= velocityofcharacter
            elif keys[2] and y < 570:
                y += velocityofcharacter
            if keys[1] and x > 0:
                x -= velocityofcharacter
            elif keys[3] and x < 800:
                x += velocityofcharacter

                
            #The hitbox
            ###########very important########################
            hitboxcol = pygame.Rect(hitbox.get_rect())
            hitboxcol.x = x
            hitboxcol.y = y
            #################################################
            #The boss hitbox
            bosshitboxcol = pygame.Rect(bosshitbox.get_rect())
            bosshitboxcol.x = 800
            bosshitboxcol.y = 200
            screen.blit(battlebackground,(0,0))
            screen.blit(bossv,(780,0))
            screen.blit(bosshitbox,(800,200))



            #if space is pressed , shoot
            if shootbullets == True and pygame.time.get_ticks()%120 >= 0 and pygame.time.get_ticks()%120 <= 5:
                bulletlist.append([x,y])
                shots += 1
            index = 0
            for eachbullet in bulletlist:
                eachbullet[0] += 10
                bulletcol = pygame.Rect(bonebullet.get_rect())
                bulletcol.x = eachbullet[0]
                bulletcol.y = eachbullet[1]
                screen.blit(bonebullet,eachbullet)
                if bulletcol.colliderect(bosshitboxcol):
                    hit += 1
                    bosshealth -= 3.5
                    bulletlist.pop(index)
                    index += 1
                if eachbullet[0]>1000:
                    bulletlist.pop(0)
            #check the status of the sansortanya and determine what character
            #did the player choose
            if sansortanya == True:
                movecharacter(sans)
            if sansortanya == False:
                movecharacter(tanya)
            screen.blit(hitbox,(x,y))
            #check the invincibility shield
            if shield1 == True and shield2 == True:
                pass
            elif shield1 == False and shield2 == True:
                invincible1 -= 1.5
            elif shield1 == False and shield2 == False:
                invincible2 -= 1.5
            #Get the current time minus the previous time
            gametime = pygame.time.get_ticks() - starttime

            """
            fullgamebullets
            """
            if gametime >= 0 and gametime <= 93000:
                try:
                    createline(bulletpos1,gametime,[800,300])
                    createline(bulletpos2,gametime,[800,300])
                    createline(bulletpos3,gametime,[800,300])
                    createline(bulletpos4,gametime,[800,300])
                    createline(bulletpos5,gametime,[800,300])
                    if linehell(hitboxcol,bulletpos1,[-1,-0.5]) == True or\
                       linehell(hitboxcol,bulletpos2,[-0.5,-1]) == True or\
                       linehell(hitboxcol,bulletpos3,[-1.5,0]) == True  or\
                       linehell(hitboxcol,bulletpos4,[-1,0.5]) == True  or\
                       linehell(hitboxcol,bulletpos5,[-0.5,1]) == True:
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                except IndexError:
                    pass
            
            """
            0:05 - 0:16
            """
            if gametime >= 5000 and gametime <= 16000:
                if onebigbullet(xvalue,onerandom,hitboxcol,1.5)[0] == True:
                    if invincible1 == 300 and invincible2 == 300:
                        live3 = False
                        shield1 = False
                    elif invincible1 <= 0 and invincible2 == 300:
                        live2 = False
                        shield2 = False
                    elif invincible1 <= 0 and invincible2 <= 0:
                        live1 = False
                if onebigbullet(xvalue,onerandom,hitboxcol,1.5)[1] == True:
                    #Randomnize the y value again and reset the x value
                    onerandom = randomshoot()
                    xvalue = [800]
            
            """
            0:16 - 0:35
            """
            if gametime >= 16000 and gametime <= 35000:
                if randomflys(hitboxcol,flylist1,0.0006,[3000,0]) == [True,False]\
                   or randomflys(hitboxcol,flylist2,0.0006,[3000,150]) == [True,False]\
                   or randomflys(hitboxcol,flylist3,0.0006,[3000,300]) == [True,False]\
                   or randomflys(hitboxcol,flylist4,0.0006,[3000,450]) == [True,False]\
                   or randomflys(hitboxcol,flylist5,0.0006,[3000,600]) == [True,False]:
                    if invincible1 == 300 and invincible2 == 300:
                        live3 = False
                        shield1 = False
                    elif invincible1 <= 0 and invincible2 == 300:
                        live2 = False
                        shield2 = False
                    elif invincible1 <= 0 and invincible2 <= 0:
                        live1 = False
                if randomflys(hitboxcol,flylist1,0.0006,[3000,0])[1] == True\
                and randomflys(hitboxcol,flylist2,0.0006,[3000,150])[1]== True\
                and randomflys(hitboxcol,flylist3,0.0006,[3000,300])[1] == True:
                    clearflylist(flylist1,3)
                    clearflylist(flylist2,3)
                    clearflylist(flylist3,3)
                    clearflylist(flylist4,3)
                    clearflylist(flylist5,3)
                    appendflylist(flylist1,3)
                    appendflylist(flylist2,3)
                    appendflylist(flylist3,3)
                    appendflylist(flylist4,3)
                    appendflylist(flylist5,3)
                


            """
            0:22 - 0:35
            """
            if gametime >= 22000 and gametime <= 35000:
                if randomflys(hitboxcol,flylist1,0.0006,[3000,0]) == [True,False]\
                   or randomflys(hitboxcol,flylist2,0.0006,[3000,150]) == [True,False]\
                   or randomflys(hitboxcol,flylist3,0.0006,[3000,300]) == [True,False]\
                   or randomflys(hitboxcol,flylist4,0.0006,[3000,450]) == [True,False]\
                   or randomflys(hitboxcol,flylist5,0.0006,[3000,600]) == [True,False]:
                    if invincible1 == 300 and invincible2 == 300:
                        live3 = False
                        shield1 = False
                    elif invincible1 <= 0 and invincible2 == 300:
                        live2 = False
                        shield2 = False
                    elif invincible1 <= 0 and invincible2 <= 0:
                        live1 = False
                if randomflys(hitboxcol,flylist1,0.0006,[3000,0])[1] == True\
                and randomflys(hitboxcol,flylist2,0.0006,[3000,150])[1]== True\
                and randomflys(hitboxcol,flylist3,0.0006,[3000,300])[1] == True:
                    clearflylist(flylist1,3)
                    clearflylist(flylist2,3)
                    clearflylist(flylist3,3)
                    clearflylist(flylist4,3)
                    clearflylist(flylist5,3)
                    appendflylist(flylist1,3)
                    appendflylist(flylist2,3)
                    appendflylist(flylist3,3)
                    appendflylist(flylist4,3)
                    appendflylist(flylist5,3)
                rowofbulletswithrandomspace(posofbullets,hitboxcol,1)
                if rowofbulletswithrandomspace(posofbullets,hitboxcol,1) == [True,False]:
                    if invincible1 == 300 and invincible2 == 300:
                        live3 = False
                        shield1 = False
                    elif invincible1 <= 0 and invincible2 == 300:
                        live2 = False
                        shield2 = False
                    elif invincible1 <= 0 and invincible2 <= 0:
                        live1 = False
                elif rowofbulletswithrandomspace(posofbullets,hitboxcol,1) == [True,True]:
                    for i in range(11):
                        randomnumber = random.randint(0,11)
                        posofbullets.pop(0)
                    posofbullets = randomnuminlist(randomnumber)
                elif rowofbulletswithrandomspace(posofbullets,hitboxcol,1) == [False,True]:
                    for i in range(11):
                        randomnumber = random.randint(0,11)
                        posofbullets.pop(0)
                    posofbullets = randomnuminlist(randomnumber)

            """
            0:35 - 0:45
            """
            if gametime >= 35000 and gametime <= 45000:
                if onebigbullet(xvalue,onerandom,hitboxcol,1)[0] == True:
                    if invincible1 == 300 and invincible2 == 300:
                        live3 = False
                        shield1 = False
                    elif invincible1 <= 0 and invincible2 == 300:
                        live2 = False
                        shield2 = False
                    elif invincible1 <= 0 and invincible2 <= 0:
                        live1 = False
                if onebigbullet(xvalue,onerandom,hitboxcol,1)[1] == True:
                    #Randomnize the y value again and reset the x value
                    onerandom = randomshoot()
                    xvalue = [800]
                if onebigbullet(xvalue,tworandom,hitboxcol,1)[0] == True:
                    if invincible1 == 300 and invincible2 == 300:
                        live3 = False
                        shield1 = False
                    elif invincible1 <= 0 and invincible2 == 300:
                        live2 = False
                        shield2 = False
                    elif invincible1 <= 0 and invincible2 <= 0:
                        live1 = False
                if onebigbullet(xvalue,tworandom,hitboxcol,1)[1] == True:
                    #Randomnize the y value again and reset the x value
                    tworandom = randomshoot()
                    xvalue = [800]
            
            """
            0:45 - 1:05
            locate player's position and shoot laser at them, which is patteren 5
            calculate the time and do the gaster blaster animation. 1.5 seconds will
            be the warning, then the next 1.5 second will be shooting
            """
            if gametime >= 45000 and gametime <= 46500:
                if gametime >= 45000 and gametime <= 45100:
                    lastx = x
                    lasty = y
                if pygame.time.get_ticks()%300 >= 0 and pygame.time.get_ticks()%300 <= 170:
                    screen.blit(warning,(lastx - 30,lasty - 50))
            if gametime >= 46500 and gametime <= 48000:
                blastereffect.play()
                if pygame.time.get_ticks()%3 == 0:
                    screen.blit(blasterlaser,(0,lasty-50))
                    screen.blit(vertlaser,(lastx-30,0))
                    vertlasercol = pygame.Rect(vertlaser.get_rect())
                    vertlasercol.x = lastx - 30
                    vertlasercol.y = 0
                    blasterlasercol = pygame.Rect(blasterlaser.get_rect())
                    blasterlasercol.x = 0
                    blasterlasercol.y = lasty - 50
                    if blasterlasercol.colliderect(hitboxcol) or vertlasercol.colliderect(hitboxcol):
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                if gametime <= 46800:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 47200:
                    screen.blit(blasteropen,(5,lasty-55))
                elif gametime <= 47400:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 48000:
                    screen.blit(blasteropen,(0,lasty-55))

            if gametime >= 48000 and gametime <= 49500:
                if gametime >= 48000 and gametime <= 48100:
                    lastx = x
                    lasty = y
                if pygame.time.get_ticks()%300 >= 0 and pygame.time.get_ticks()%300 <= 170:
                    screen.blit(warning,(lastx - 30,lasty - 50))
            if gametime >= 49500 and gametime <= 51000:
                blastereffect.play()
                if pygame.time.get_ticks()%3 == 0:
                    screen.blit(blasterlaser,(0,lasty-50))
                    screen.blit(vertlaser,(lastx-30,0))
                    vertlasercol = pygame.Rect(vertlaser.get_rect())
                    vertlasercol.x = lastx - 30
                    vertlasercol.y = 0
                    blasterlasercol = pygame.Rect(blasterlaser.get_rect())
                    blasterlasercol.x = 0
                    blasterlasercol.y = lasty - 50
                    if blasterlasercol.colliderect(hitboxcol) or vertlasercol.colliderect(hitboxcol):
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                if gametime <= 49800:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 50200:
                    screen.blit(blasteropen,(5,lasty-55))
                elif gametime <= 50400:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 51000:
                    screen.blit(blasteropen,(0,lasty-55))

            if gametime >= 51000 and gametime <= 52500: 
                if gametime >= 51000 and gametime <= 51100:
                    lastx = x
                    lasty = y
                if pygame.time.get_ticks()%300 >= 0 and pygame.time.get_ticks()%300 <= 170:
                    screen.blit(warning,(lastx - 30,lasty - 50))
            if gametime >= 52500 and gametime <= 54000:
                blastereffect.play()
                if pygame.time.get_ticks()%3 == 0:
                    screen.blit(blasterlaser,(0,lasty-50))
                    screen.blit(vertlaser,(lastx-30,0))
                    vertlasercol = pygame.Rect(vertlaser.get_rect())
                    vertlasercol.x = lastx - 30
                    vertlasercol.y = 0
                    blasterlasercol = pygame.Rect(blasterlaser.get_rect())
                    blasterlasercol.x = 0
                    blasterlasercol.y = lasty - 50
                    if blasterlasercol.colliderect(hitboxcol) or vertlasercol.colliderect(hitboxcol):
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                if gametime <= 52800:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 53200:
                    screen.blit(blasteropen,(5,lasty-55))
                elif gametime <= 53400:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 54000:
                    screen.blit(blasteropen,(0,lasty-55))


            if gametime >= 54000 and gametime <= 55500: 
                if gametime >= 54000 and gametime <= 54100:
                    lastx = x
                    lasty = y
                if pygame.time.get_ticks()%300 >= 0 and pygame.time.get_ticks()%300 <= 170:
                    screen.blit(warning,(lastx - 30,lasty - 50))
            if gametime >= 55500 and gametime <= 57000:
                blastereffect.play()
                if pygame.time.get_ticks()%3 == 0:
                    screen.blit(blasterlaser,(0,lasty-50))
                    screen.blit(blasterlaser,(0,lasty-50))
                    screen.blit(vertlaser,(lastx-30,0))
                    vertlasercol = pygame.Rect(vertlaser.get_rect())
                    vertlasercol.x = lastx - 30
                    vertlasercol.y = 0
                    blasterlasercol = pygame.Rect(blasterlaser.get_rect())
                    blasterlasercol.x = 0
                    blasterlasercol.y = lasty - 50
                    if blasterlasercol.colliderect(hitboxcol) or vertlasercol.colliderect(hitboxcol):
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                if gametime <= 55800:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 56200:
                    screen.blit(blasteropen,(5,lasty-55))
                elif gametime <= 56400:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 57000:
                    screen.blit(blasteropen,(0,lasty-55))

            if gametime >= 57000 and gametime <= 58500: 
                if gametime >= 57000 and gametime <= 57100:
                    lastx = x
                    lasty = y
                if pygame.time.get_ticks()%300 >= 0 and pygame.time.get_ticks()%300 <= 170:
                    screen.blit(warning,(lastx - 30,lasty - 50))
            if gametime >= 58500 and gametime <= 60000:
                blastereffect.play()
                if pygame.time.get_ticks()%3 == 0:
                    screen.blit(blasterlaser,(0,lasty-50))
                    screen.blit(vertlaser,(lastx-30,0))
                    vertlasercol = pygame.Rect(vertlaser.get_rect())
                    vertlasercol.x = lastx - 30
                    vertlasercol.y = 0
                    blasterlasercol = pygame.Rect(blasterlaser.get_rect())
                    blasterlasercol.x = 0
                    blasterlasercol.y = lasty - 50
                    if blasterlasercol.colliderect(hitboxcol) or vertlasercol.colliderect(hitboxcol):
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                if gametime <= 58800:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 59200:
                    screen.blit(blasteropen,(5,lasty-55))
                elif gametime <= 59400:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 60000:
                    screen.blit(blasteropen,(0,lasty-55))

            if gametime >= 60000 and gametime <= 61500: 
                if gametime >= 60000 and gametime <= 60100:
                    lastx = x
                    lasty = y
                if pygame.time.get_ticks()%300 >= 0 and pygame.time.get_ticks()%300 <= 170:
                    screen.blit(warning,(lastx - 30,lasty - 50))
            if gametime >= 61500 and gametime <= 63000:
                blastereffect.play()
                if pygame.time.get_ticks()%3 == 0:
                    screen.blit(blasterlaser,(0,lasty-50))
                    screen.blit(vertlaser,(lastx-30,0))
                    vertlasercol = pygame.Rect(vertlaser.get_rect())
                    vertlasercol.x = lastx - 30
                    vertlasercol.y = 0
                    blasterlasercol = pygame.Rect(blasterlaser.get_rect())
                    blasterlasercol.x = 0
                    blasterlasercol.y = lasty - 50
                    if blasterlasercol.colliderect(hitboxcol) or vertlasercol.colliderect(hitboxcol):
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                if gametime <= 61800:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 62200:
                    screen.blit(blasteropen,(5,lasty-55))
                elif gametime <= 62400:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 63000:
                    screen.blit(blasteropen,(0,lasty-55))

            if gametime >= 63000 and gametime <= 64500: 
                if gametime >= 63000 and gametime <= 63100:
                    lastx = x
                    lasty = y
                if pygame.time.get_ticks()%300 >= 0 and pygame.time.get_ticks()%300 <= 170:
                    screen.blit(warning,(lastx - 30,lasty - 50))
            if gametime >= 64500 and gametime <= 66000:
                blastereffect.play()
                if pygame.time.get_ticks()%3 == 0:
                    screen.blit(blasterlaser,(0,lasty-50))
                    screen.blit(vertlaser,(lastx-30,0))
                    vertlasercol = pygame.Rect(vertlaser.get_rect())
                    vertlasercol.x = lastx - 30
                    vertlasercol.y = 0
                    blasterlasercol = pygame.Rect(blasterlaser.get_rect())
                    blasterlasercol.x = 0
                    blasterlasercol.y = lasty - 50
                    if blasterlasercol.colliderect(hitboxcol) or vertlasercol.colliderect(hitboxcol):
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                if gametime <= 64800:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 65200:
                    screen.blit(blasteropen,(5,lasty-55))
                elif gametime <= 65400:
                    screen.blit(blasterclose,(0,lasty-50))
                elif gametime <= 66000:
                    screen.blit(blasteropen,(0,lasty-55))
            """
            1:06 - 1:21
            """
            if gametime >= 66000 and gametime <= 81000:
                rowofbulletswithrandomspace(posofbullets,hitboxcol,1)
                if rowofbulletswithrandomspace(posofbullets,hitboxcol,1) == [True,False]:
                    if invincible1 == 300 and invincible2 == 300:
                        live3 = False
                        shield1 = False
                    elif invincible1 <= 0 and invincible2 == 300:
                        live2 = False
                        shield2 = False
                    elif invincible1 <= 0 and invincible2 <= 0:
                        live1 = False
                elif rowofbulletswithrandomspace(posofbullets,hitboxcol,1) == [True,True]:
                    for i in range(11):
                        randomnumber = random.randint(0,11)
                        posofbullets.pop(0)
                    posofbullets = randomnuminlist(randomnumber)
                elif rowofbulletswithrandomspace(posofbullets,hitboxcol,1) == [False,True]:
                    for i in range(11):
                        randomnumber = random.randint(0,11)
                        posofbullets.pop(0)
                    posofbullets = randomnuminlist(randomnumber)
                if randomflys(hitboxcol,flylist1,0.0006,[3000,0]) == [True,False]\
                   or randomflys(hitboxcol,flylist3,0.0006,[3000,300]) == [True,False]\
                   or randomflys(hitboxcol,flylist5,0.0006,[3000,600]) == [True,False]:
                    if invincible1 == 300 and invincible2 == 300:
                        live3 = False
                        shield1 = False
                    elif invincible1 <= 0 and invincible2 == 300:
                        live2 = False
                        shield2 = False
                    elif invincible1 <= 0 and invincible2 <= 0:
                        live1 = False
                if randomflys(hitboxcol,flylist1,0.0006,[3000,0])[1] == True\
                and randomflys(hitboxcol,flylist3,0.0006,[3000,300])[1] == True:
                    clearflylist(flylist1,2)
                    clearflylist(flylist3,2)
                    clearflylist(flylist5,2)
                    appendflylist(flylist1,2)
                    appendflylist(flylist3,2)
                    appendflylist(flylist5,2)
            """
            1:21 - 1:33
            """
            if gametime >= 81000 and gametime <= 93000:
                if onebigbullet(xvalue,onerandom,hitboxcol,1.5)[0] == True:
                    if invincible1 == 300 and invincible2 == 300:
                        live3 = False
                        shield1 = False
                    elif invincible1 <= 0 and invincible2 == 300:
                        live2 = False
                        shield2 = False
                    elif invincible1 <= 0 and invincible2 <= 0:
                        live1 = False
                if onebigbullet(xvalue,onerandom,hitboxcol,1.5)[1] == True:
                    #Randomnize the y value again and reset the x value
                    onerandom = randomshoot()
                    xvalue = [800]
                if onebigbullet(xvalue,tworandom,hitboxcol,1)[0] == True:
                    if invincible1 == 300 and invincible2 == 300:
                        live3 = False
                        shield1 = False
                    elif invincible1 <= 0 and invincible2 == 300:
                        live2 = False
                        shield2 = False
                    elif invincible1 <= 0 and invincible2 <= 0:
                        live1 = False
                if onebigbullet(xvalue,tworandom,hitboxcol,1)[1] == True:
                    #Randomnize the y value again and reset the x value
                    tworandom = randomshoot()
                    xvalue = [800]
            """
            1:33 - 1:55
            """
            if gametime >= 93000 and gametime <= 97000 or\
               gametime >= 101000 and gametime <= 105000 or\
               gametime >= 107000 and gametime <= 111000 or\
               gametime >= 110000 and gametime <= 115000:
                try:
                    createline(bulletpos1,gametime,[800,400])
                    createline(bulletpos2,gametime,[800,400])
                    createline(bulletpos3,gametime,[800,400])
                    createline(bulletpos4,gametime,[800,400])
                    createline(bulletpos5,gametime,[800,400])
                    if linehell(hitboxcol,bulletpos1,[-1,-0.5]) == True or\
                       linehell(hitboxcol,bulletpos2,[-0.5,-1]) == True or\
                       linehell(hitboxcol,bulletpos3,[-1.5,0]) == True  or\
                       linehell(hitboxcol,bulletpos4,[-1,0.5]) == True  or\
                       linehell(hitboxcol,bulletpos5,[-0.5,1]) == True:
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                except IndexError:
                    pass
            if gametime >= 95000 and gametime <= 99000 or\
               gametime >= 99000 and gametime <= 103000 or\
               gametime >= 103000 and gametime <= 107000 or\
               gametime >= 113000 and gametime <= 115000:
                try:
                    createline(bulletpos1,gametime,[800,300])
                    createline(bulletpos2,gametime,[800,300])
                    createline(bulletpos3,gametime,[800,300])
                    createline(bulletpos4,gametime,[800,300])
                    createline(bulletpos5,gametime,[800,300])
                    if linehell(hitboxcol,bulletpos1,[-1,-0.5]) == True or\
                       linehell(hitboxcol,bulletpos2,[-0.5,-1]) == True or\
                       linehell(hitboxcol,bulletpos3,[-1.5,0]) == True  or\
                       linehell(hitboxcol,bulletpos4,[-1,0.5]) == True  or\
                       linehell(hitboxcol,bulletpos5,[-0.5,1]) == True:
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                except IndexError:
                    pass
            if gametime >= 97000 and gametime <= 111000 or\
               gametime >= 105000 and gametime <= 109000 or\
               gametime >= 109000 and gametime <= 113000:
                try:
                    createline(bulletpos1,gametime,[800,200])
                    createline(bulletpos2,gametime,[800,200])
                    createline(bulletpos3,gametime,[800,200])
                    createline(bulletpos4,gametime,[800,200])
                    createline(bulletpos5,gametime,[800,200])
                    if linehell(hitboxcol,bulletpos1,[-1,-0.5]) == True or\
                       linehell(hitboxcol,bulletpos2,[-0.5,-1]) == True or\
                       linehell(hitboxcol,bulletpos3,[-1.5,0]) == True  or\
                       linehell(hitboxcol,bulletpos4,[-1,0.5]) == True  or\
                       linehell(hitboxcol,bulletpos5,[-0.5,1]) == True:
                        if invincible1 == 300 and invincible2 == 300:
                            live3 = False
                            shield1 = False
                        elif invincible1 <= 0 and invincible2 == 300:
                            live2 = False
                            shield2 = False
                        elif invincible1 <= 0 and invincible2 <= 0:
                            live1 = False
                except IndexError:
                    pass
            if cheat == True:
                #the cheat mode makes lives always True
                if invincible1 <= 0:
                    live1 = True
                    live2 = True
                    live3 = True
                    invincible1 = 300
                    invincible2 = 300
                    died += 1
            if bosshealth <= 300:
                screen.blit(healthbar6,(1000,100))
            elif bosshealth <= 600:
                screen.blit(healthbar5,(1000,100))
            elif bosshealth <= 900:
                screen.blit(healthbar4,(1000,100))
            elif bosshealth <= 1200:
                screen.blit(healthbar3,(1000,100))
            elif bosshealth <= 1500:
                screen.blit(healthbar2,(1000,100))
            elif bosshealth <= 1800:
                screen.blit(healthbar,(1000,100))
            if live1:
                screen.blit(heart,(0,0))
            if live2:
                screen.blit(heart,(40,0))
            if live3:
                screen.blit(heart,(80,0))
            if live1 == False:
                revolovania.stop()
                wahwahwah.play()
                for i in range(1000):
                    screen.blit(youdied,(350,200))
                    pygame.display.update()
                badendingloop = True
                break
            if gametime <= 115000:
                gametimetext = font.render("timeleft: "+ str(round((115000-gametime)/120000))+":"+str(round((115000-gametime)/1000%60)).zfill(2), True, (255,0,0))
                screen.blit(gametimetext,(910,10))
            else:
                playScreen = False
            bosshealthtext = font.render('''bosshealth:%d'''%(round(bosshealth)),True,(255,255,255))
            screen.blit(bosshealthtext,(910,30))
            pygame.display.update()
        
        if bosshealth <= 0:
            goodendingloop = True
        if bosshealth <= -100:
            bossoverdead = True
        try:
            accuracy = round(((hit/shots)*100),2)
        except ZeroDivisionError:
            accuracy = 0
        if goodendingloop == False and badendingloop == False:
            normalendingloop = True
        """
        The results
        """
        if bossoverdead == True and accuracy == 100:
            rating = "SS"
            results = True
        elif bossoverdead == True and accuracy >= 95:
            rating = "S"
            results = True
        elif bossoverdead == True or accuracy >= 95:
            rating = "A"
            results = True
        elif accuracy >= 80:
            rating = "B"
            results = True
        elif accuracy >= 60:
            rating = "C"
            results = True
        elif accuracy >= 0:
            rating = "D"
            results = True
        if badendingloop == True:
            rating = "F"
            results = True
        #this code checks if the main loop is false. If it is, that means the player
        #chooses to quit the game, so the results loop need to be False in
        #order for the game to quit. 
        
        if mainloop == False:
            results = False
        #This variable is True if the boss is dead and the bosshealth <= -100(meaning that
        #the player dealts more than 1900 damage)
        #if boss is "dead"(the health bar is empty),the player will enter
        #the happy ending
        #if boss health is above 0 when the agme ends, the player will enter the normal ending regardless the acuracy
        quietwater.play()
        while results:
            while badendingloop:
                screen.blit(badending,(0,0))
                bosshealthtext = font.render(rating,True,(255,255,255))
                screen.blit(f,(0,400))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key==K_a:
                            badendingloop = False
                            results = False
                            mainScreen = False
                            playScreen = False
                            mainloop = False
                #The player who died automatically get an "F"
            while normalendingloop:
                screen.blit(normalending,(0,0))
                if rating == "SS":
                    screen.blit(ss,(0,400))
                if rating == "S":
                    screen.blit(s,(0,400))
                if rating == "A":
                    screen.blit(a,(0,400))
                if rating == "B":
                    screen.blit(b,(0,400))
                if rating == "C":
                    screen.blit(c,(0,400))
                if rating == "D":
                    screen.blit(d,(0,400))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key==K_a:
                            normalendingloop = False
                            results = False
                            mainScreen = False
                            playScreen = False
                            mainloop = False
                #The player gets a rating sheet
            while goodendingloop:
                screen.blit(goodending,(0,0))
                if rating == "SS":
                    screen.blit(ss,(0,400))
                if rating == "S":
                    screen.blit(s,(0,400))
                if rating == "A":
                    screen.blit(a,(0,400))
                if rating == "B":
                    screen.blit(b,(0,400))
                if rating == "C":
                    screen.blit(c,(0,400))
                if rating == "D":
                    screen.blit(d,(0,400))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key==K_a:
                            goodendingloop = False
                            results = False
                            mainScreen = False
                            playScreen = False
                            mainloop = False


                #The player gets a rating sheet
    quietwater.stop()
print("After pressing the cheat mode button, you should have died "+ str(died)\
      + " times. ")
print("Your accuracy is:" + str(accuracy))
print("Bosshealth left: " + str(bosshealth))
pygame.quit()
