import random # For generating random numbers
import sys # We will use sys.exit to exit the program
import pygame
import button
from pygame.locals import * # Basic pygame imports
from pygame import mixer

FPS = 30
SCREENWIDTH = 720
SCREENHEIGHT = 420
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME_SPRITES = {}
GAME_SOUNDS = {}
points =0
basketposx =0
basketposy =0
volume = 0.5
a='30'
b='60'
c='90'


#welcome screen

def welcomeScreen():
    notificationx = int(GAME_SPRITES['notification'].get_width())/2
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_ESCAPE):
                gamepause()
            elif event.type==KEYDOWN and (event.key==K_SPACE):
                return
            else :
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['notification'], ((360-notificationx), 210))
                SCREEN.blit(GAME_SPRITES['basket'], (360, 340))
                pygame.display.update()
                FPSCLOCK.tick(FPS)



def mainGame():
    GAME_SOUNDS['background'].play()
    GAME_SOUNDS['background'].set_volume(volume)

    basketx = 360
    baskety = 340
    basketwidth = int(GAME_SPRITES['basket'].get_width())
    black=False
    red=False
    red1=False
    black1=False
    secondapple=False
    #to maintain the position of basket after game over
    global points
    global basketposx
    global basketposy

    #random apple position generation 
    applex = randomapple()
    appley = -17
    applex1 = randomapple()
    appley1 = -17
    applevel = 3
    score = 0
    collosion = 0

    #random apple color generation
    applecolor=randomcolor()
    applecolor1=randomcolor()
    applerando = [
        applecolor
    ]
    applerando1 = [
        applecolor1
    ]

    pro = [3,5,7,9] #probablity of getting black apple


    #game loop start
    while True:
        basketx1,baskety1 = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and event.key == K_ESCAPE:
                GAME_SOUNDS['background'].stop()
                gamepause()
                
            else :
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['basket'], (basketx1, baskety))

        #random black or red apple generation for apple 1
        for applerand in applerando:
            if applerand in pro:
                SCREEN.blit(GAME_SPRITES['blackapple'], (applex,appley))
                black=True

            else :
                SCREEN.blit(GAME_SPRITES['apple'], (applex,appley))
                red=True
        #to maintain the gap between  apple when speed become high automatically 
        c=-17
        #movement control for apple 1
        if appley<345:
            appley+=applevel
            
        #new apple generation if last pop out
        if appley>345:
            if black:
                collosion-=1
                black=False
            collosion+=1
            if red:
                GAME_SOUNDS['die'].play()
                GAME_SOUNDS['die'].set_volume(volume)
            newapple=randomapple()
            applex=newapple
            newappley=c
            c-=2
            appley=newappley
            newapplecolor = randomcolor()
            applerando.pop()
            applerando.append(newapplecolor)
            
        #check score for apple 1
        if (applex in range(basketx1,basketx1+basketwidth)) and (appley > 340) :
            if black:
                GAME_SOUNDS['hit'].play()
                GAME_SOUNDS['hit'].set_volume(volume)
                collosion += 1
                score-=1
                black=False
            score += 1
            if red:
                GAME_SOUNDS['point'].play()
                GAME_SOUNDS['point'].set_volume(volume)
                red=False
            applevel+=0.1
            newapple=randomapple()
            applex=newapple
            newappley=c
            c-=2
            appley=newappley
            newapplecolor = randomcolor()
            applerando.pop()
            applerando.append(newapplecolor)

            
        if appley>225:
            secondapple=True

        if secondapple:
            #random black or red apple generation for apple 2
            for applerand in applerando1:
                if applerand in pro:
                    SCREEN.blit(GAME_SPRITES['blackapple'], (applex1,appley1))
                    black1=True

                else :
                    SCREEN.blit(GAME_SPRITES['apple'], (applex1,appley1))
                    red1=True
                

            #movement control for apple 2
            if appley1<345:
                appley1+=applevel
            a=-17
            #new apple generation if last pop out
            if appley1>345:
                if black1:
                    collosion-=1
                    black1=False
                collosion+=1
                if red1:
                    GAME_SOUNDS['die'].play()
                    GAME_SOUNDS['die'].set_volume(volume)
                newapple1=randomapple()
                applex1= newapple1
                newappley1=a
                a-=1
                appley1=newappley1
                newapplecolor1 = randomcolor()
                applerando1.pop()
                applerando1.append(newapplecolor1)

            #check score for apple 2
            if (applex1 in range(basketx1,basketx1+basketwidth)) and (appley1 > 340) :
                if black1:
                    GAME_SOUNDS['hit'].play()
                    GAME_SOUNDS['hit'].set_volume(volume)
                    collosion += 1
                    score-=1
                    black1=False
                score += 1
                if red1:
                    GAME_SOUNDS['point'].play()
                    GAME_SOUNDS['point'].set_volume(volume)
                    red1=False
                applevel+=0.1
                newapple1=randomapple()
                applex1= newapple1
                newappley1=a
                a-=1
                appley1=newappley1
                newapplecolor1 = randomcolor()
                applerando1.pop()
                applerando1.append(newapplecolor1)

        if collosion == 0:
            col=123
        if collosion == 1:
            col=12
        if collosion == 2:
            col=1
        if collosion == 3:
            GAME_SOUNDS['swoosh'].play()
            GAME_SOUNDS['swoosh'].set_volume(volume)
            GAME_SOUNDS['background'].stop()
            return


        #score print
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()

            
        #highscore
        try:
            highscore = int(gethighscore())
        except:
            highscore = 0
            
        #check highscore
        if highscore<score:
            highscore=score
        with open("highscore.txt","w")as f:
            f.write(str(highscore)) 
            
        #highscore print
        myDigits = [int(x) for x in list(str(highscore))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = 600

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, 20))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()

        #life print
        myDigits = [int(x) for x in list(str(col))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = 0

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, 0))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        points=score
        basketposx=basketx1
        basketposy=baskety
        #speed of apple increase
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

#random apple position generation module
def randomapple():
    x=random.randrange(0,700)
    return x

#random apple color generation module
def randomcolor():
    x=random.randrange(0,10)
    return x

#when game is over
def gameover():
    notificationx = int(GAME_SPRITES['notification2'].get_width())/2
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and event.key == K_ESCAPE:
                gameovergamepause()
            elif event.type==KEYDOWN and (event.key==K_SPACE):
                return
            else :
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['notification2'], ((360-notificationx), 210))
                SCREEN.blit(GAME_SPRITES['basket'], (basketposx, basketposy))

            

            myDigits = [int(x) for x in list(str(points))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
            
#game setting
def gamepause():
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    newgame_button = button.Button(240, 110, GAME_SPRITES['newgame'], 1)
    resume_button = button.Button(269, 35, GAME_SPRITES['resume'], 1)
    difficulty_button = button.Button(236, 180, GAME_SPRITES['difficulty'], 1)
    options_button = button.Button(262, 260, GAME_SPRITES['options'], 1)
    quit_button = button.Button(307, 328, GAME_SPRITES['quit'], 1)
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_ESCAPE):
                GAME_SOUNDS['background'].play()
                return
            elif event.type==KEYDOWN and (event.key==K_SPACE):
                GAME_SOUNDS['background'].play()
                return
            else :
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                if newgame_button.draw(screen):
                    mainGame()
                if resume_button.draw(screen):
                    return
                if difficulty_button.draw(screen):
                    difficulty()
                if options_button.draw(screen):
                    options()
                if quit_button.draw(screen):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def gameovergamepause():
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    newgame_button = button.Button(244, 110, GAME_SPRITES['newgame'], 1)
    difficulty_button = button.Button(236, 180, GAME_SPRITES['difficulty'], 1)
    options_button = button.Button(262, 260, GAME_SPRITES['options'], 1)
    quit_button = button.Button(307, 328, GAME_SPRITES['quit'], 1)
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_ESCAPE):
                GAME_SOUNDS['background'].play()
                return
            elif event.type==KEYDOWN and (event.key==K_SPACE):
                GAME_SOUNDS['background'].play()
                return
            else :
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                if newgame_button.draw(screen):
                    mainGame()
                if difficulty_button.draw(screen):
                    difficulty()
                if options_button.draw(screen):
                    options()
                if quit_button.draw(screen):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def difficulty():
    global FPS
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    easy_button = button.Button(120, 132, GAME_SPRITES['easy'], 1)
    normal_button = button.Button(260, 128, GAME_SPRITES['normal'], 1)
    hard_button = button.Button(460, 132, GAME_SPRITES['hard'], 1)
    back_button = button.Button(307, 223, GAME_SPRITES['back'], 1)
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif back_button.draw(screen):
                return
            else :
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                if easy_button.draw(screen):
                    FPS =30
                    return
                if normal_button.draw(screen):
                    FPS =60
                    return
                if hard_button.draw(screen):
                    FPS =90
                    return
                if back_button.draw(screen):
                    pass
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def options():
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    fps_button = button.Button(307, 130, GAME_SPRITES['fps'], 1)
    audio_button = button.Button(290, 60, GAME_SPRITES['audio'], 1)
    back_button = button.Button(307, 219, GAME_SPRITES['back'], 1)
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif back_button.draw(screen):
                return
            else :
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                if audio_button.draw(screen):
                    audio()
                if fps_button.draw(screen):
                    fps()
                if back_button.draw(screen):
                    pass
        pygame.display.update()
        FPSCLOCK.tick(FPS)           
def audio():
    global volume
    vol = 1
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    easy_button = button.Button(120, 105, GAME_SPRITES['easy'], 1)
    normal_button = button.Button(260, 101, GAME_SPRITES['normal'], 1)
    hard_button = button.Button(460, 105, GAME_SPRITES['hard'], 1)
    back_button = button.Button(307, 255, GAME_SPRITES['back'], 1)
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif back_button.draw(screen):
                return
            else :
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                if easy_button.draw(screen):
                    vol=0.2
                    volume = vol
                    return
                if normal_button.draw(screen):
                    vol=0.5
                    volume = vol
                    return
                if hard_button.draw(screen):
                    vol=1
                    volume = vol
                    return
                if back_button.draw(screen):
                    pass
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def fps():
    global FPS
    global a
    global b
    global c
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    fps1_button = button.Button(250, 192, GAME_SPRITES[a], 1)
    fps2_button = button.Button(340, 192, GAME_SPRITES[b], 1)
    fps3_button = button.Button(430, 192, GAME_SPRITES[c], 1)
    back_button = button.Button(307, 265, GAME_SPRITES['back'], 1)
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif back_button.draw(screen):
                return
            else :
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                if fps1_button.draw(screen):
                    a='301'
                    b='60'
                    c='90'
                    FPS =30
                    return
                if fps2_button.draw(screen):
                    a='30'
                    b='601'
                    c='90'
                    FPS =60
                    return
                if fps3_button.draw(screen):
                    a='30'
                    b='60'
                    c='901'
                    FPS =90
                    return
                if back_button.draw(screen):
                    pass 
        pygame.display.update()
        FPSCLOCK.tick(FPS)      

def gethighscore():
    with open("highscore.txt","r")as f:
        return f.read()

if __name__ == "__main__":
    pygame.init() # Initialize all pygame's modules
    pygame.mixer.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Fruit basket')
    GAME_SPRITES['background'] = pygame.image.load('sprites/backround.png').convert()
    GAME_SPRITES['notification'] = pygame.image.load('sprites/notification.png').convert()
    GAME_SPRITES['notification2'] = pygame.image.load('sprites/notification2.png').convert()
    GAME_SPRITES['basket'] = pygame.image.load('sprites/basket.png').convert()
    GAME_SPRITES['apple'] = pygame.image.load('sprites/apple.png').convert()
    GAME_SPRITES['blackapple'] = pygame.image.load('sprites/blackapple.png').convert()
    GAME_SPRITES['resume'] = pygame.image.load('sprites/buttons/resume.png').convert()
    GAME_SPRITES['difficulty'] = pygame.image.load('sprites/buttons/difficulty.png').convert()
    GAME_SPRITES['options'] = pygame.image.load('sprites/buttons/options.png').convert()
    GAME_SPRITES['quit'] = pygame.image.load('sprites/buttons/quit.png').convert()
    GAME_SPRITES['fps'] = pygame.image.load('sprites/buttons/fps.png').convert()
    GAME_SPRITES['back'] = pygame.image.load('sprites/buttons/back.png').convert()
    GAME_SPRITES['30'] = pygame.image.load('sprites/fps/30.png').convert()
    GAME_SPRITES['60'] = pygame.image.load('sprites/fps/60.png').convert()
    GAME_SPRITES['90'] = pygame.image.load('sprites/fps/90.png').convert()
    GAME_SPRITES['301'] = pygame.image.load('sprites/fps/301.png').convert()
    GAME_SPRITES['601'] = pygame.image.load('sprites/fps/601.png').convert()
    GAME_SPRITES['901'] = pygame.image.load('sprites/fps/901.png').convert()
    GAME_SPRITES['easy'] = pygame.image.load('sprites/buttons/easy.png').convert()
    GAME_SPRITES['normal'] = pygame.image.load('sprites/buttons/normal.png').convert()
    GAME_SPRITES['hard'] = pygame.image.load('sprites/buttons/hard.png').convert()
    GAME_SPRITES['newgame'] = pygame.image.load('sprites/buttons/newgame.png').convert()
    GAME_SPRITES['audio'] = pygame.image.load('sprites/buttons/audio.png').convert()

    GAME_SPRITES['numbers'] = (
        pygame.image.load('sprites/numbers/0.png').convert_alpha(),
        pygame.image.load('sprites/numbers/1.png').convert_alpha(),
        pygame.image.load('sprites/numbers/2.png').convert_alpha(),
        pygame.image.load('sprites/numbers/3.png').convert_alpha(),
        pygame.image.load('sprites/numbers/4.png').convert_alpha(),
        pygame.image.load('sprites/numbers/5.png').convert_alpha(),
        pygame.image.load('sprites/numbers/6.png').convert_alpha(),
        pygame.image.load('sprites/numbers/7.png').convert_alpha(),
        pygame.image.load('sprites/numbers/8.png').convert_alpha(),
        pygame.image.load('sprites/numbers/9.png').convert_alpha(),
    )

    # Game sounds
    GAME_SOUNDS['background'] = pygame.mixer.Sound('sprites/audio/background.mp3')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('sprites/audio/hit.mp3')
    GAME_SOUNDS['die'] = pygame.mixer.Sound('sprites/audio/die.mp3')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('sprites/audio/point.mp3')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('sprites/audio/swoosh.mp3')


    while True:
        welcomeScreen() # Shows welcome screen to the user until he presses a button
        while True:
            mainGame() # This is the main game function
            gameover()
    