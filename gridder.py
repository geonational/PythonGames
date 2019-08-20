#-------------------------------------------------------------------------------
# Name:        frogs
# Purpose:
#
# Author:      semoslin
#
# Created:     23/11/2012
# Copyright:   (c) semoslin 2012
# Licence:     None
#-------------------------------------------------------------------------------

import random,pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
BOXSIZE = 70
GAPSIZE = 10
BOARDHEIGHT = 6
BOARDWIDTH = 9
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

BLACK = (0,0,0)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
WHITE = ( 0,0,0)
MINTCREAM = (245,255,250)
AZURE = (240,255,255)
ALICEBLUE = (240,248,255)
IVORY = (255,255,240)

COLORLIST = (MINTCREAM,AZURE,ALICEBLUE,IVORY)

BOXCOLOR = GREEN
HIGHLIGHTCOLOR = RED

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'



def main():

    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Frog!')

    # These are the Max Left and Right postions for the x positions, used for all the lanes
    laneRight,laneLeft = laneStartEnd()

    lane1x = 0
    lane1y = 0
    lane1Img = pygame.image.load('cat.png').convert_alpha()
    lane1Width = lane1Img.get_width()
    lane1y = topOfLane(1)
    # This lane moves to the left so we start at the right positon
    lane1x = laneRight
    #print "Cat width is "  + str(lane1Width)

    lane2x = 0
    lane2y = 0
    lane2Img = pygame.image.load('truckb.png').convert_alpha()
    lane2Width = lane2Img.get_width()
    lane2y = topOfLane(2)
    # This lane moves to the right so we start at the left positon
    lane2x = laneLeft


    lane3x = 0
    lane3y = 0
    lane3Img = pygame.image.load('cat.png').convert_alpha()
    lane3Width = lane3Img.get_width()
    lane3y = topOfLane(3)
    # This lane moves to the left so we start at the right positon
    lane3x = laneRight

    lane4x = 0
    lane4y = 0
    lane4Img = pygame.image.load('dumptruckb.png').convert_alpha()
    lane4Width = lane4Img.get_width()
    lane4y = topOfLane(4)
    # This lane moves to the right so we start at the left positon
    lane4x = laneLeft


    frogRemain = 3
    screenLevel = 1

    #Start position for frog
    frogBoxx,frogBoxy = 2,0
    frogImg = pygame.image.load('frog_80t.png').convert_alpha()
    explosionImg = pygame.image.load('explosion80.png').convert_alpha()

    BGCOLOR =  MINTCREAM

    DISPLAYSURF.fill(BGCOLOR)

    # Display some text


    while True: # main game loop
        DISPLAYSURF.fill(BGCOLOR)
        drawLanes()
        mouseClicked = False

        # Lane 1
        if (lane1x >= laneLeft):
                DISPLAYSURF.blit(lane1Img, (lane1x, lane1y))
                lane1x -= 1

        else:
                lane1x = laneRight


        # Lane 2
        if (lane2x <= laneRight):
                DISPLAYSURF.blit(lane2Img, (lane2x, lane2y))
                lane2x += 2
                #print catx,caty
        else:
                lane2x = laneLeft


        # Lane 3
        if (lane3x >= laneLeft):
                DISPLAYSURF.blit(lane1Img, (lane3x, lane3y))
                lane3x -= 3
                #print catx,caty
        else:
                lane3x = laneRight

        # Lane 4
        if (lane4x <= laneRight):
                DISPLAYSURF.blit(lane4Img, (lane4x, lane4y))
                lane4x += 3
                #print catx,caty
        else:
                lane4x = laneLeft

        frogx,frogy = leftTopCoordsOfBox(frogBoxx,frogBoxy)
        DISPLAYSURF.blit(frogImg, (frogx, frogy))

        # Section to check is frog has been hit
        if frogBoxy == 1:
            boxx, boxy = getBoxAtPixel(lane1x, lane1y,frogBoxy,0)
           # drawHighlightBox(boxx, boxy)
            if (boxx == frogBoxx) and (boxy == frogBoxy):
                        frogRemain -= 1
                        oneLessFrog(boxx,boxy,explosionImg,frogRemain)
                        frogBoxx,frogBoxy = 2,0

        elif frogBoxy == 2:
            boxx, boxy = getBoxAtPixel(lane2x, lane2y,frogBoxy,lane2Width)
            #drawHighlightBox(boxx, boxy)
            if (boxx == frogBoxx) and (boxy == frogBoxy):
                        frogRemain -= 1
                        oneLessFrog(boxx,boxy,explosionImg,frogRemain)
                        frogBoxx,frogBoxy = 2,0

        elif frogBoxy == 3:
            boxx, boxy = getBoxAtPixel(lane3x, lane3y,frogBoxy,0)
            if (boxx == frogBoxx) and (boxy == frogBoxy):
                        frogRemain -= 1
                        oneLessFrog(boxx,boxy,explosionImg,frogRemain)
                        frogBoxx,frogBoxy = 2,0

        elif frogBoxy == 4:
            boxx, boxy = getBoxAtPixel(lane4x, lane4y,frogBoxy,lane4Width)
            if (boxx == frogBoxx) and (boxy == frogBoxy):
                        frogRemain -= 1
                        oneLessFrog(boxx,boxy,explosionImg,frogRemain)
                        frogBoxx,frogBoxy = 2,0

        elif frogBoxy == 5:
            screenLevel += 1
            #Level is complete, go through color list, need to go through in order
            BGCOLOR = random.choice(COLORLIST)
            frogBoxx,frogBoxy = 2,0

        displayScore(frogRemain,screenLevel)

        for event in pygame.event.get():

            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):

                pygame.quit()
                sys.exit()






            elif event.type == KEYUP:
             # check if the user pressed a key to slide a tile


                if event.key in (K_LEFT, K_a) and checkLeftBoxx(frogBoxx):
                    frogBoxx -= 1
                elif event.key in (K_RIGHT, K_d) and checkRightBoxx(frogBoxx):
                    frogBoxx += 1
                elif event.key in (K_UP, K_w) and checkTopBoxy(frogBoxy):
                    frogBoxy -= 1
                elif event.key in (K_DOWN, K_s):
                    frogBoxy += 1
               # elif event.key == K_b:
                #      frogx, frogy = CentiodCoordsOfBox(0,0)







        pygame.display.update()
            #pygame.time.wait(1000)
        FPSCLOCK.tick(FPS)


def getBoxAtPixel(x, y,fLane,imgOffset):
    #The box the frog is in and the box  the opponent in are checked for intersection.
    # The imgOffset is needed for images moving to the right so the intersection will calculated
    # at the right side of the image

    for boxx in range(BOARDWIDTH):

            boxy = fLane
            left, top = leftTopCoordsOfBox(boxx, boxy)

            boxRect = pygame.Rect(left, top, (BOXSIZE + GAPSIZE), (BOXSIZE + GAPSIZE))

            if boxRect.collidepoint((x + imgOffset), y):

                return (boxx, boxy)

    return (None, None)


def leftTopCoordsOfBox(boxx, boxy):
# Convert board coordinates to pixel coordinates

    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)


def CentiodCoordsOfBox(boxx, boxy):
# Convert board coordinates to box centriod

    xcenter = boxx * (BOXSIZE + GAPSIZE) + XMARGIN + ((BOXSIZE + GAPSIZE)/2)
    ycenter = boxy * (BOXSIZE + GAPSIZE) + YMARGIN  + ((BOXSIZE + GAPSIZE)/2)
    return (xcenter, ycenter)


#This is only for testing
def drawHighlightBox(HLboxx, HLboxy):

    left, top = leftTopCoordsOfBox(HLboxx, HLboxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left , top, BOXSIZE + 10, BOXSIZE + 10), 0)
    print "drawing box"


def drawExplosion(boxx,boxy,explosionImg):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    DISPLAYSURF.blit(explosionImg, (left, top))


def topOfLane(lane):
        # We may not end of using this
        # Convert board coordinates to pixel coordinates
            topX = YMARGIN + ((BOXSIZE + GAPSIZE) * lane)
            return (topX)



def laneStartEnd ():
        laneStart = (((BOXSIZE + GAPSIZE) * BOARDWIDTH ) + XMARGIN)
        laneEnd = laneStart - ((BOXSIZE + GAPSIZE) * BOARDWIDTH )
        return laneStart,laneEnd

def displayScore(frogRemain,screenLevel):
        font = pygame.font.Font(None, 24)
        text = font.render("Frogs Remaining  " + str(frogRemain) , 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.y,textpos.centerx =  10,DISPLAYSURF.get_rect().centerx
        DISPLAYSURF.blit(text, textpos)

        text1 = font.render("Level  " + str(screenLevel) , 1, (10, 10, 10))
        textpos1 = text1.get_rect()
        textpos1.y,textpos1.centerx =  30,DISPLAYSURF.get_rect().centerx
        DISPLAYSURF.blit(text1, textpos1)


def drawLanes ():
    xLaneStart = XMARGIN
    xLaneFinish = (WINDOWWIDTH - XMARGIN)
    yLaneBoth = YMARGIN # Lanes are always horizontal

    for laneCount in range(BOARDHEIGHT):
        pygame.draw.line(DISPLAYSURF,BLACK,(xLaneStart,yLaneBoth),(xLaneFinish,yLaneBoth))
        yLaneBoth += (BOXSIZE + GAPSIZE)


def resetFrog ():
    # The frog got hit so we need to reset.
    # Do we need to put a message or flash the screen red?
    frogRemain -= 1
    frogBoxx,frogBoxy = 2,0


def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def waitReturn():
    while 1:
        inkey = get_key()
        if inkey == K_RETURN:
            break

def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor):
    # pick a font you have and set its size
    myfont = pygame.font.SysFont(Textfont, Textsize)
    # apply it to text on a label
    label = myfont.render(txtText, 1, Textcolor)
    # put the label object on the screen at point Textx, Texty
    DISPLAYSURF.blit(label, (Textx, Texty))
    # show the whole thing
    pygame.display.flip()


def oneLessFrog(boxx,boxy,explosionImg,frogRemain):
    drawExplosion(boxx,boxy,explosionImg)
    if frogRemain == 0:
        printText("No more Frogs left!", "MS Comic Sans", 30, 200, 75, RED)
        printText("GAME OVER", "MS Comic Sans", 30, 200, 95, RED)
        waitReturn()
        pygame.quit()
        sys.exit()
    else:
         printText("You lost your frog!!", "MS Comic Sans", 30, 200, 75, RED)
         printText("Press Enter to Continue", "MS Comic Sans", 30, 200, 95, RED)
         waitReturn()

#These three functions stop frog from moving off the board

def checkRightBoxx(boxxEdge):
    #To check edge conditions for frog
    if (boxxEdge < (BOARDWIDTH - 1)):
        return True

def checkLeftBoxx(boxxEdge):
    #To check edge conditions for frog
    if (boxxEdge > 0):
        return True

def checkTopBoxy(boxyEdge):
    #To check top edge conditions for frog
    if (boxyEdge > 0):
        return True

# run the main block
if __name__ == '__main__':

  main()